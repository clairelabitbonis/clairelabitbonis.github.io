---
title: "Useful gists"
date: 2022-07-16
description: "Useful gists."
summary: "Useful gists."

draft: true
math: true 
highlight: true
hightlight_languages: ["python","bash"]

authors: ["Claire Labit-Bonis"]

hero: 

tags: []

menu:
  sidebar:
    name: Shortcodes
    identifier: shortcodes
    parent: 
    weight: 20
---

## Git
### Add submodule
- cd themes/
- git submodule add https:// github.com/< theme >

### Remove submodule
- Delete the relevant section from the .gitmodules file.
- Stage the .gitmodules changes git add .gitmodules
- Delete the relevant section from .git/config.
- Run git rm --cached path_to_submodule (no trailing slash).
- Run rm -rf .git/modules/path_to_submodule (no trailing slash).
- Commit git commit -m "Removed submodule "
- Delete the now untracked submodule files rm -rf path_to_submodule