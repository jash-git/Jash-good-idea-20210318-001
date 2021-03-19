Outfile test.exe
Requestexecutionlevel user

!include nsDialogs.nsh

Page Custom mypagecreate mypageleave
Page Instfiles

Function mypagecreate
Var /Global MyTextbox
nsDialogs::Create /NOUNLOAD 1018
Pop $0
${NSD_CreateText} 10% 20u 80% 12u "Hello World"
Pop $MyTextbox
nsDialogs::Show
FunctionEnd

Function mypageleave
${NSD_GetText} $MyTextbox $0
MessageBox mb_ok $0
Abort ;Don't move to next page (If the input was invalid etc)
FunctionEnd

Section
SectionEnd