Readme
=====

This repo is the markdown based wiki website.  To edit it, you can clone the repo using github, edit the local markdown files, and sync them back up to this repo -- that's all it takes to update the website.

**Note**:  The github wiki for the repo (link at right) is **not** part of the website!  Editing it won't change the website!

The markdown wiki supports the github flavor or markdown. Markdown (and maybe MDWiki in particular) has inconistent support for  inline HTML so some of the old pages are broken.

One thing we should think hard about is how to consistently format the lessons pages so they are easy to navigate. The exsiting stuff is all over the map, none of the things I experimented with seemed very good. We can also do simple 'next' and 'back' buttons but I'd like to do more  if possible.


When formatting links, MDWiki produces urls that look like this: `http://techartmafia.github.io/#!**your-link-here.md**`, where **your-link-here** is the relative link from the root of the site.  Your links don't have to include that whole thing: for links to other wiki pages just provide the relative path to the .md file of the page: \[for example\]\(crs/glossary.md) will link to the `glossary.md` page in the `crs` directory.  For links outside of this site, the [regular markdown style](http://daringfireball.net/projects/markdown/syntax) of square-bracket text followed by parenthesized links works fine.

