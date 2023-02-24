;;; lisp/init.el -*- lexical-binding: t; -*-
;;; Commentary:
;;
;; :core is now treated like a normal module, and this is its (temporary) init
;; file, which will be removed once we've resolved our `use-package' dependency
;; (which will soon be moved to its own module), then these will be returned to
;; the profile init file.
;;
;;; Code:

(doom-require 'doom-keybinds)
(doom-require 'doom-ui)
(doom-require 'doom-projects)
(doom-require 'doom-editor)

(add-to-list 'custom-theme-load-path "~/.emacs.d/everforest-theme")
(load-theme 'everforest-hard-dark t)
;;; init.el ends here
