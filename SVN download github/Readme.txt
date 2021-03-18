使用SVN ~ 下載github專案中的某個資料夾或者檔案

資料來源: https://www.itread01.com/content/1545682523.html
http://subversion.apache.org/packages.html#windows [ VisualSVN (32- and 64-bit client and server; supported and maintained by VisualSVN)]


比如要下載: https://github.com/jash-git/richie_jQuery_EasyUI/tree/master/jashliao_Ex

方法:
01.將“tree/master”改成“trunk”
	https://github.com/jash-git/richie_jQuery_EasyUI/tree/master/jashliao_Ex

02.下載
	.\bin\svn.exe checkout https://github.com/jash-git/richie_jQuery_EasyUI/trunk/jashliao_Ex
	pause

PS.如果遇到非純英文路徑，就要透過短網址功能來作弊[克服 SVN: E170000: 錯誤]
	https://github.com/jash-git/Jash-good-idea-20210318-001/trunk/GitZip%E6%95%99%E5%AD%B8
	https://bit.ly/30Wd6nM
