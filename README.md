# obsidian_to_hugo
**Features: Obsidian wikilink, img, video to hugo ref, figure, video.**  
**Tested on Windows 11(Supporting Windows!)**

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
Only image and video is supported for `![[~~]]`. If not image, it is assume to be video.

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
