#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^SPACE::  Winset, Alwaysontop, , A
^y:: 
Sendinput, ^{c} ; copy the selected text/item/whatever
clipwait, 1,1
Current_Clipboard := Clipboard

Run, chrome.exe "https://www.google.com/search?q=%Current_Clipboard%" " --new-window "


