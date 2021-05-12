" Keeping extra files in one directory [ // makes file names include paths to avoid collisions]
set backupdir=$HOME/.vim/backup//
set directory=$HOME/.vim/swap//
set undodir=$HOME/.vim/undo//
" Force to keep these files
set backup
set swapfile
set undofile

" For line numbers
set nu
set relativenumber

" Tabs and spaces
set tabstop=4 softtabstop=4
set shiftwidth=4
set noexpandtab

" Do highlight search queries
set hlsearch
set incsearch
" change highlight colors
hi Search ctermbg=236
hi Search ctermfg=LightGray

" Opening multiple buffers in vim without saving each
set hidden

" Search queries ignorecase when all is small. Not when something is capital
set smartcase
set ignorecase

" Set scroll margin to 8 lines
set scrolloff=8
