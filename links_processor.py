# Original Source: https://github.com/devidw/obsidian-to-hugo/blob/master/src/wiki_links_processor.py
# Modified by MilkClouds

import re, shutil
from pathlib import Path


def get_links(text: str, args) -> list:
    """
    Get all wiki links from the given text and return a list of them.
    Each list item is a dictionary with the following keys:
    - wiki_link: the exact match
    - link: the extracted link
    - text: the possible extracted text
    """
    wiki_links = []
    attachments = []
    wiki_link_regex = r'([!]?)\[\[(.*?)\]\]'
    for match in re.finditer(wiki_link_regex, text):
        out = {
            "wiki_link": match.group(),
            'type': "ref"
        }

        if '|' in match.group(2):
            out['link'], out['text'] = match.group(2).split('|')
        else:
            out['link'] = match.group(2)
            out['text'] = match.group(2)

        # if the link ends with `_index` remove it
        if out['link'].endswith('_index'):
            out['link'] = out['link'][:-6]

        # match = re.match('^(.*?)\.(.*)$', out['link'])
        if match.group(1):
            attachments.append(out['link'])
            if out['link'].lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                out['type'] = 'figure'
            else:
                out['type'] = 'video'

            out['link'] = Path.joinpath(Path.relative_to(args.hugo_attachments_dir, Path.joinpath(args.hugo_dir, "static")), out['link']).as_posix()
            out['link'] = '/' + out['link']

        wiki_links.append(out)
    return wiki_links, attachments


def build_hugo_links(links: list, args) -> list:
    """
    Extens the passed wiki links list by adding a dict key for the hugo link.
    """
    for link in links:
        if link['type'] == 'ref':
            link['hugo_link'] = f'[{link["text"]}]({{{{< ref "{link["link"]}" >}}}})'
        else:
            if link['type'] == 'figure':
                link['hugo_link'] = f'{{{{< {link["type"]} src="{link["link"]}" alt="{link["text"]}" >}}}}'
            else:
                link['hugo_link'] = f'{{{{< {link["type"]} src="{link["link"]}" >}}}}'
    return links


def replace_links(text: str, links: list) -> str:
    """
    Replace all wiki links with hugo links in the given text.
    """
    for link in links:
        text = text.replace(link['wiki_link'], link['hugo_link'])
    return text

def copy_attachments(attachments: list, args):
    for file in attachments:
        shutil.copyfile(Path.joinpath(args.obsidian_attachments_dir, file), Path.joinpath(args.hugo_attachments_dir, file))

def replace_links_helper(text: str, args) -> str:
    """
    Helper function for replace_wiki_links.
    """
    links, attachments = get_links(text, args)
    links = build_hugo_links(links, args)
    copy_attachments(attachments, args)
    return replace_links(text, links)