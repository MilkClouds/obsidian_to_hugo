# obsidian_to_hugo
**Obsidian wikilink, img, video to hugo ref, figure, video.**  
**Tested on Windows 11(Supporting Windows!)**

# Usage
`python convert.py`

# Feature
Obsidian wikilink, img, video to hugo ref, figure, video. **Refer to Demo below.**

Only obsidian attachments which is mentioned on content is copied to hugo attachment folder.

Hugo Content, Hugo Attachments, Obsidian Attachments, Obsidian Contents, ..., **everything** is not removed by running this program.  
**It do not execute removal command.**  
But override by copy can be occured. If you misuse this several time(e.g. changing file name and run this several time) there may exist many unused files, so be cautious about this.

# Arguments
```
    parser.add_argument("--hugo-dir", default = Path("../blog"))
    parser.add_argument("--hugo-content-dir", default = Path("../blog/content/post/"))
    parser.add_argument("--hugo-attachments-dir", default = Path("../blog/static/attachments/"))
    parser.add_argument("--obsidian-content-dir", default = Path("./blog/"))
    parser.add_argument("--obsidian-attachments-dir", default = Path("./Attachments/"))
```
configure obsidian attachment folder and hugo attachment folder path by your own. It will be copied to hugo_attachments_dir.

Example: "./Attachments/1.png" to "../blog/static/attachments/1.png"

# Warning
Only image and video is supported for `![[~~]]`. **If it is not image, it is assumed to be video, even if it isn't.**

File attachment is not supported for now. I've searched [this hugo shortcode](https://learn.netlify.app/en/shortcodes/attachments/), and considering this to implement.

## Demo
Input
```
[[test2]]
![[Trim.mp4]]
![[Pasted image 20220524212151.png]]
```

Output
```
[test2]({{< ref "test2" >}})
{{< video src="/attachments/Trim.mp4" >}}
{{< figure src="/attachments/Pasted image 20220524212151.png" alt="Pasted image 20220524212151.png" >}}
```


## Thanks to
https://github.com/devidw/obsidian-to-hugo/
