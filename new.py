import re


filename="model3.dat"
filename2="model2.dat"


f = open(filename)
lines = f.readlines()
f.close()

f = open(filename2, 'w')
for line in lines:
    f.write(line[1:])
f.close()

if __name__=="__main__":
    with open('model2.dat', 'r') as f:
        data = f.read()

#reExp = re.compile("=", flags=re.S)
reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)

#reExp = re.compile("\s*(\w+)\s*=\s*([+-.\w]+)\s*", flags=re.S)

extLst = dict(reExp.findall(data))

print(extLst)

print(extLst["tr"])
print(extLst["swedge"])

print(extLst["swgeo"])
print(extLst["vfbo"])

print(extLst["rsh"])
print(extLst["rsw1"])


parlist=[
'LEVEL      ',
'SCALELEV   ',
'VERSION    ',
'TYPE       ',
'TR         ',
'SWGIDL     ',
'SWIGATE    ',
'SWIMPACT   ',
'SWJUNASYM  ',
'SWJUNCAP   ',
'SWJUNEXP   ',
'A1L        ',
'A1O        ',
'A1W        ',
'A2O        ',
'A3L        ',
'A3O        ',
'A3W        ',
'A4L        ',
'A4O        ',
'A4W        ',
'AGIDLDW    ',
'AGIDLW     ',
'ALP1L1     ',
'ALP1L2     ',
'ALP1LEXP   ',
'ALP1W      ',
'ALP2L1     ',
'ALP2L2     ',
'ALP2LEXP   ',
'ALP2W      ',
'ALPL       ',
'ALPLEXP    ',
'ALPW       ',
'AXL        ',
'AXO        ',
'BETW1      ',
'BETW2      ',
'BGIDLDO    ',
'BGIDLO     ',
'CBBTBOT    ',
'CBBTBOTD   ',
'CBBTGAT    ',
'CBBTGATD   ',
'CBBTSTI    ',
'CBBTSTID   ',
'CFBO       ',
'CFL        ',
'CFLEXP     ',
'CFRDW      ',
'CFRW       ',
'CFW        ',
'CGBOVL     ',
'CGIDLDO    ',
'CGIDLO     ',
'CHIBO      ',
'CJORBOT    ',
'CJORBOTD   ',
'CJORGAT    ',
'CJORGATD   ',
'CJORSTI    ',
'CJORSTID   ',
'CSL        ',
'CSLEXP     ',
'CSLW       ',
'CSO        ',
'CSRHBOT    ',
'CSRHBOTD   ',
'CSRHGAT    ',
'CSRHGATD   ',
'CSRHSTI    ',
'CSRHSTID   ',
'CSW        ',
'CTATBOT    ',
'CTATBOTD   ',
'CTATGAT    ',
'CTATGATD   ',
'CTATSTI    ',
'CTATSTID   ',
'CTL        ',
'CTLEXP     ',
'CTLW       ',
'CTO        ',
'CTW        ',
'DLQ        ',
'DLSIL      ',
'DNSUBO     ',
'DPHIBL     ',
'DPHIBLEXP  ' ,
'DPHIBLW    ' ,
'DPHIBO     ' ,
'DPHIBW     ' ,
'DTA        ',
'DWQ        ',
'EFO        ',
'EPSROXO    ',
'FBBTRBOT   ',
'FBBTRBOTD  ',
'FBBTRGAT   ',
'FBBTRGATD  ',
'FBBTRSTI   ',
'FBBTRSTID  ',
'FBET1      ',
'FBET1W     ',
'FBET2      ',
'FETAO      ',
'FJUNQ      ',
'FJUNQD     ' ,
'FNTO       ',
'FOL1       ',
'FOL2       ',
'GC2O       ',
'GC3O       ' ,
'GCOO       ' ,
'IDSATRBOT  ' ,
'IDSATRBOTD ',
'IDSATRGAT  ',
'IDSATRGATD ',
'IDSATRSTI  ',
'IDSATRSTID ',
'IGINVLW    ',
'IGOVDW     ',
'IGOVW      ',
'IMAX       ',
'KUO        ',
'KUOWEL     ' ,
'KUOWELW    ' ,
'KUOWEO     ',
'KUOWEW     ',
'KVSAT      ',
'KVTHO      ',
'KVTHOWEL   ',
'KVTHOWELW  ',
'KVTHOWEO   ',
'KVTHOWEW   ',
'LAP        ',
'LINTNOI    ',
'LKUO       ',
'LKVTHO     ',
'LLODKUO    ',
'LLODVTH    ',
'LODETAO    ',
'LOV        ',
'LOVD       ',
'LP1        ',
'LP1W       ',
'LP2        ',
'LPCK       ',
'LPCKW      ',
'LVARL      ',
'LVARO      ',
'LVARW      ',
'MEFFTATBOT ',
'MEFFTATBOTD',
'MEFFTATGAT ',
'MEFFTATGATD',
'MEFFTATSTI ',
'MEFFTATSTID',
'MUEO       ',
'MUEW       ',
'NFALW      ',
'NFBLW      ',
'NFCLW      ',
'NOVDO      ',
'NOVO       ',
'NPCK       ',
'NPCKW      ',
'NPL        ',
'NPO        ',
'NSLPO      ',
'NSUBO      ',
'NSUBW      ',
'PBOT       ',
'PBOTD      ',
'PBRBOT     ',
'PBRBOTD    ',
'PBRGAT     ',
'PBRGATD    ',
'PBRSTI     ',
'PBRSTID    ',
'PGAT       ',
'PGATD      ',
'PHIGBOT    ',
'PHIGBOTD   ',
'PHIGGAT    ',
'PHIGGATD   ',
'PHIGSTI    ',
'PHIGSTID   ',
'PKUO       ',
'PKVTHO     ',
'PSTI       ',
'PSTID      ',
'QMC        ',
'RBULKO     ',
'RGO        ',
'RINT       ',
'RJUNSO     ',
'RJUNDO     ',
'RSBO       ',
'RSGO       ',
'RSHG       ',
'RSW1       ',
'RSW2       ',
'RVPOLY     ',
'RWELLO     ',
'SAREF      ',
'SBREF      ',
'SCREF      ',
'STA2O      ',
'STBETL     ',
'STBETLW    ',
'STBETO     ',
'STBETW     ',
'STBGIDLDO  ',
'STBGIDLO   ',
'STCSO      ',
'STETAO     ',
'STFBBTBOT  ',
'STFBBTBOTD ',
'STFBBTGAT  ',
'STFBBTGATD ',
'STFBBTSTI  ',
'STFBBTSTID ',
'STIGO      ',
'STMUEO     ',
'STRSO      ',
'STTHEMUO   ',
'STTHESATL  ',
'STTHESATLW ',
'STTHESATO  ',
'STTHESATW  ',
'STVFBL     ',
'STVFBLW    ',
'STVFBO     ',
'STVFBW     ',
'STXCORO    ',
'THEMUO     ',
'THESATBO   ',
'THESATGO   ',
'THESATL    ',
'THESATLEXP ',
'THESATLW   ',
'THESATO    ',
'THESATW    ',
'TKUO       ',
'TOXO       ',
'TOXOVDO    ',
'TOXOVO     ',
'TRJ        ',
'UO         ',
'VBIRBOT    ',
'VBIRBOTD   ',
'VBIRGAT    ',
'VBIRGATD   ',
'VBIRSTI    ',
'VBIRSTID   ',
'VBRBOT     ',
'VBRBOTD    ',
'VBRGAT     ',
'VBRGATD    ',
'VBRSTI     ',
'VBRSTID    ',
'VFBL       ',
'VFBLW      ',
'VFBO       ',
'VFBW       ',
'VJUNREF    ',
'VJUNREFD   ',
'VNSUBO     ',
'VPO        ',
'WBET       ',
'WEB        ',
'WEC        ',
'WKUO       ',
'WKVTHO     ',
'WLOD       ',
'WLODKUO    ',
'WLODVTH    ',
'WOT        ',
'WSEG       ',
'WSEGP      ',
'WVARL      ',
'WVARO      ',
'WVARW      ',
'XCORL      ',
'XCORLW     ',
'XCORO      ',
'XCORW      ',
'XJUNGAT    ',
'XJUNGATD   ',
'XJUNSTI    ',
'XJUNSTID   '
]

print(parlist)

print(parlist[1])
print(parlist[0])

print(parlist[6])
print(parlist[8])

print(extLst["level"])
x=0

sorted_parlist=[x.strip(' ') for x in parlist]
print(sorted_parlist)
print(parlist)

"""
for item in parlist:
    item.strip()
    print(item)

print(parlist)


"""



for param in (sorted_parlist):
 #   print(param)
    for item in extLst:
        print(item)
 #       print (x)
        x=x+1
        if item.upper() == param:
            print(item)
            print("true")
            print(item.val)

#    for y in len(extLst):
 #       if


#print(extLst)

