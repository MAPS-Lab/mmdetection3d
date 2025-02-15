import filecmp
from pathlib import Path
import mmcv
import os


copies = [
    '20220126-15-12-26/input/radar_polar/1/1643181755777(1).csv',
    '20220126-15-12-26/input/radar_polar/1/1643181755699(1).csv',
    '20220126-15-02-25/input/radar_polar/4/1643180597925(1).csv',
    '20220126-15-22-27/input/radar_polar/1/1643182104357(1).csv',
    '20220126-15-22-27/input/radar_polar/1/1643182104292(1).csv',
    '20220126-15-22-27/input/radar_polar/0/1643182379350(1).csv',
    '20220126-15-42-29/input/radar_polar/1/1643183081647(1).csv',
    '20220126-15-42-29/input/radar_polar/4/1643183091466(1).csv',
    '20220126-15-42-29/input/radar_polar/4/1643183375993(1).csv',
    '20220126-15-42-29/input/radar_polar/0/1643183282886(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971717(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182570594(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970870(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182974905(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516744(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516833(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182557746(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182594073(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969690(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970811(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182973705(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970949(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516685(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970736(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969854(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182968615(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571192(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971378(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182974960(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182594127(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571049(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969744(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971114(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182680399(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516560(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182603666(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971198(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571541(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182517091(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516505(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516450(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971322(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182395988(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516896(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182633258(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182625537(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182972292(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969799(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971892(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970626(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182591663(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182974727(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182972427(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571637(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182570899(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182557951(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970681(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182517147(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969318(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971059(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571483(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971464(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182559271(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182593991(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571339(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182968962(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969982(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970059(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182974781(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971603(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182591609(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516958(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182559422(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971265(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971836(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182570448(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970113(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182516615(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182970572(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182592212(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971658(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182971004(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969617(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182974519(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969374(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182571394(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182969928(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182559183(1).csv',
    '20220126-15-32-28/input/radar_polar/1/1643182517222(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552068(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182873191(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552123(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182820616(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182813389(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182930973(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182451308(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182551958(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702182(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702241(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552233(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703067(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182860218(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182932678(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182933785(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182851960(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182491752(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182813161(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552563(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702682(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182551903(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182814782(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703342(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702463(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703012(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182419931(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701463(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182964592(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703562(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182872531(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552178(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182730700(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702517(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182886228(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552508(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182730816(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182620207(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552013(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701907(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182782363(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182561142(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182813443(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552288(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702847(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182815442(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702017(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182818471(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702296(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702405(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182851740(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701188(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182872476(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182933722(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182776310(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552453(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182813847(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182560812(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703727(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182930533(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703122(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702350(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702792(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182419876(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182813051(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182451554(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701133(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702572(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182820561(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701519(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552343(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182452161(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182703397(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182702737(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182727913(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182491080(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182544589(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701628(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182701852(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552618(1).csv',
    '20220126-15-32-28/input/radar_polar/4/1643182552398(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182610589(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567467(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182385455(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182610699(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869440(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866580(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182844973(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866800(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437654(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182871475(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869385(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182843649(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567302(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869275(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182566747(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869055(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869110(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182871365(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182386335(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182878395(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182878285(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182397665(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866690(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866305(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182610644(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182436936(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182388755(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869330(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182398215(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182901000(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182672589(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869605(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182878855(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182871420(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567191(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182901766(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182952475(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869550(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866965(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567357(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182878913(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182831335(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182966225(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866360(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182387545(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182907259(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182386390(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866525(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182901891(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866415(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437597(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182900279(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182867185(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437768(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866470(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437476(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182901822(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866635(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869495(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437535(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869000(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182900774(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869770(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182815165(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182871530(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182831940(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869220(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182566692(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182714283(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567689(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182416623(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182879188(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182753229(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182906531(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182437709(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869715(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182675002(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182869165(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182566637(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182865975(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182753158(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866855(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182899729(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182867010(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182567909(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182396290(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866745(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182867075(1).csv',
    '20220126-15-32-28/input/radar_polar/0/1643182866250(1).csv',
    '20220126-15-32-28/input/image/B/1643182897438_B(1).png',
    '20220126-15-32-28/input/image/B/1643182898038_B(1).png',
    '20220126-15-32-28/input/image/B/1643182902339_B(1).png',
    '20220126-15-32-28/input/image/B/1643182839541_B(1).png',
    '20220126-15-32-28/input/image/B/1643182606638_B(1).png',
    '20220126-15-32-28/input/image/B/1643182896939_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607838_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607738_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373641_B(1).png',
    '20220126-15-32-28/input/image/B/1643182896639_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373441_B(1).png',
    '20220126-15-32-28/input/image/B/1643182929738_B(1).png',
    '20220126-15-32-28/input/image/B/1643182800843_B(1).png',
    '20220126-15-32-28/input/image/B/1643182606738_B(1).png',
    '20220126-15-32-28/input/image/B/1643182374141_B(1).png',
    '20220126-15-32-28/input/image/B/1643182837541_B(1).png',
    '20220126-15-32-28/input/image/B/1643182840141_B(1).png',
    '20220126-15-32-28/input/image/B/1643182372641_B(1).png',
    '20220126-15-32-28/input/image/B/1643182374241_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373541_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607938_B(1).png',
    '20220126-15-32-28/input/image/B/1643182928838_B(1).png',
    '20220126-15-32-28/input/image/B/1643182809142_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607338_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373841_B(1).png',
    '20220126-15-32-28/input/image/B/1643182608038_B(1).png',
    '20220126-15-32-28/input/image/B/1643182901339_B(1).png',
    '20220126-15-32-28/input/image/B/1643182802043_B(1).png',
    '20220126-15-32-28/input/image/B/1643182897339_B(1).png',
    '20220126-15-32-28/input/image/B/1643182901838_B(1).png',
    '20220126-15-32-28/input/image/B/1643182929439_B(1).png',
    '20220126-15-32-28/input/image/B/1643182805243_B(1).png',
    '20220126-15-32-28/input/image/B/1643182809442_B(1).png',
    '20220126-15-32-28/input/image/B/1643182811841_B(1).png',
    '20220126-15-32-28/input/image/B/1643182608238_B(1).png',
    '20220126-15-32-28/input/image/B/1643182774943_B(1).png',
    '20220126-15-32-28/input/image/B/1643182371041_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607638_B(1).png',
    '20220126-15-32-28/input/image/B/1643182813041_B(1).png',
    '20220126-15-32-28/input/image/B/1643182901438_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373241_B(1).png',
    '20220126-15-32-28/input/image/B/1643182800743_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373941_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373341_B(1).png',
    '20220126-15-32-28/input/image/B/1643182808643_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373741_B(1).png',
    '20220126-15-32-28/input/image/B/1643182896739_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373041_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607238_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607138_B(1).png',
    '20220126-15-32-28/input/image/B/1643182928938_B(1).png',
    '20220126-15-32-28/input/image/B/1643182928339_B(1).png',
    '20220126-15-32-28/input/image/B/1643182928139_B(1).png',
    '20220126-15-32-28/input/image/B/1643182930039_B(1).png',
    '20220126-15-32-28/input/image/B/1643182897039_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607038_B(1).png',
    '20220126-15-32-28/input/image/B/1643182606938_B(1).png',
    '20220126-15-32-28/input/image/B/1643182897239_B(1).png',
    '20220126-15-32-28/input/image/B/1643182901538_B(1).png',
    '20220126-15-32-28/input/image/B/1643182896839_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607538_B(1).png',
    '20220126-15-32-28/input/image/B/1643182373141_B(1).png',
    '20220126-15-32-28/input/image/B/1643182901738_B(1).png',
    '20220126-15-32-28/input/image/B/1643182608138_B(1).png',
    '20220126-15-32-28/input/image/B/1643182607438_B(1).png',
    '20220126-15-32-28/input/image/B/1643182803943_B(1).png',
    '20220126-15-32-28/input/image/B/1643182929839_B(1).png',
    '20220126-15-32-28/input/image/B/1643182606838_B(1).png',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182751500(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182586400(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182712400(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182657900(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182712000(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182712200(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182618000(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182710800(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182485600(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182445200(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182712300(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182711800(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182654300(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182654400(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182751600(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182751400(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182711900(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182751700(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182783300(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182750900(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182711600(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182712100(1).pcd',
    '20220126-15-32-28/input/lidar/20220126-15-32-28_C/1643182631400(1).pcd',
    '20220126-14-52-23/input/radar_polar/1/1643180185952(1).csv',
    '20220126-14-52-23/input/radar_polar/4/1643180450830(1).csv',
    '20220126-14-52-23/input/radar_polar/4/1643180568471(1).csv',
    '20220126-14-52-23/input/radar_polar/4/1643180528597(1).csv',
    '20220126-14-52-23/input/radar_polar/4/1643180528758(1).csv',
    '20220126-14-52-23/input/radar_polar/4/1643180562813(1).csv',
    '20220126-14-52-23/input/image/B/1643180181537_B(1).png',
    '20220126-14-52-23/input/lidar/20220126-14-52-23_C/1643180013000(1).pcd',
    '20220126-14-52-23/input/lidar/20220126-14-52-23_C/1643180024800(1).pcd',
    '20220126-14-52-23/input/lidar/20220126-14-52-23_C/1643180262000(1).pcd',
    '20220126-14-52-23/input/lidar/20220126-14-52-23_C/1643180013500(1).pcd',
    '20220118-13-43-20/input/image/B/964395_B(1).png',
    '20220118-13-43-20/input/image/B/959995_B(1).png',
    '20220118-13-43-20/input/image/B/966095_B(1).png',
    '20220118-13-43-20/input/image/B/965195_B(1).png',
]

root = Path('/') / 'home' / 'winstmakerr11' / 'Downloads' / 'inhouse'

def handle(copy):
    copy_path = root / copy
    orig_path = copy_path.parent / f'{copy_path.stem[:-3]}{copy_path.suffix}'
    if not os.path.exists(orig_path):
        raise ValueError(orig_path)
    # if not filecmp.cmp(copy_path, orig_path, shallow=False):
    #     raise ValueError(orig_path)
    # os.remove(copy_path)

def main():
    for copy in mmcv.track_iter_progress(copies):
        handle(copy)

if __name__ == '__main__':
    main()