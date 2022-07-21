# Sample setup for [neovim 0.7+](https://github.com/neovim/neovim)
## Prerequisites
1. Install [neovim](https://neovim.io/)
2. Install [python-neovim](https://pypi.org/project/python-neovim/)
3. Install [pynvim](https://pypi.org/project/pynvim/)
5. Install [biber](https://en.wikibooks.org/wiki/LaTeX/Bibliographies_with_biblatex_and_biber)
6. Install [ctags](http://ctags.sourceforge.net/)

## Neovim setup
* Somewhere in the init.vim put the following codes:
```
function! RunLuaLatex(TexFileName)
  let g:asyncrun_exit = 'silent :lua require("notify")("Lualatex has done~! -- Le", "info")'
  " normal! :w!<cr>
  exec "w!"
  " echom "Run Lualatex now..."
  let execstr="AsyncRun! lualatex --shell-escape --synctex=1 " . a:TexFileName
  " echom execstr
  silent exec execstr
  let bibfile=split(a:TexFileName,"\\.")[0] . "_biber.bib"
  " echom bibfile
  if filereadable(bibfile)
    let execstr="!ctags -R --options=/home/lechen/Dropbox/mydotfiles/ctags/ctags_latex *.tex " . bibfile
    silent exec execstr
  elseif filereadable("All.bib")
    let execstr="!ctags -R --options=/home/lechen/Dropbox/mydotfiles/ctags/ctags_latex *.tex All.bib"
    silent exec execstr
  else
    echom "No bib files and ctags has not run~! -- Le Chen"
  endif
  " echom execstr
  " let g:asyncrun_exit = 'silent :lua require("notify")("Asyncrun has done~!", "info")'
endfunction
autocmd FileType tex noremap <silent> <leader><leader> :call RunLuaLatex(expand("%"))<cr>

function! LatexBiber()
  " echom "Run biber now..."
  let g:asyncrun_exit = 'silent :lua require("notify")("Biber has done~! -- Le", "info")'
  let filenameRoot=expand("%:r")
  let execstr="AsyncRun! biber --output_format=bibtex --output_resolve " . filenameRoot. ".bcf && biber " . filenameRoot
  echom execstr
  exec execstr
  echom "Done biber now..."
  " let g:asyncrun_exit = 'silent :lua require("notify")("Asyncrun has done~!", "info")'
endfunction
autocmd FileType tex noremap <leader>b :update<bar>:call LatexBiber()<CR>
```

* Here is the ctags_latex file:
```
--langdef=tex2
--langmap=tex2:.tex
--regex-tex2=/\\label[ \t]*\*?\{[ \t]*([^}]*)\}/\1/l,label/

--langdef=bib
--langmap=bib:.bib
--regex-bib=/^@[A-Za-z]+\{([^,]*)/\1/b,bib/
```

* `<leader>b` to run `biber`
* `<leader><leader>` to run `lualatex`
* You need to run once lualatex, followed by once biber, then run twice lualatex to see the results.
