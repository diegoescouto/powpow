import requests
import re
from urllib.parse import quote_plus, quote
from bs4 import BeautifulSoup
import base64

def canais_list(server):
    canais = [
        {
            "id": "iptv:canal1",
            "type": "tv",
            "name": "✦●✦ GENERAL ✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ GENERAL ✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171283.m3u8",
                    "title": "✦●✦ GENERAL ✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal2",
            "type": "tv",
            "name": "BR| AMC HD",
            "poster": f"{server}https://lo1.in/BR/amc.png",
            "background": f"{server}https://lo1.in/BR/amc.png",
            "description": "Canal BR| AMC HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162303.m3u8",
                    "title": "BR| AMC HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal3",
            "type": "tv",
            "name": "BR| ANHANGUERA GOIANIA",
            "poster": f"{server}https://lo1.in/BR/anhago.png",
            "background": f"{server}https://lo1.in/BR/anhago.png",
            "description": "Canal BR| ANHANGUERA GOIANIA ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162391.m3u8",
                    "title": "BR| ANHANGUERA GOIANIA",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal4",
            "type": "tv",
            "name": "BR| ARTE 1 HD",
            "poster": f"{server}https://lo1.in/BR/art.png",
            "background": f"{server}https://lo1.in/BR/art.png",
            "description": "Canal BR| ARTE 1 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171325.m3u8",
                    "title": "BR| ARTE 1 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal5",
            "type": "tv",
            "name": "BR| BAHIA HD",
            "poster": f"{server}https://lo1.in/BR/bahia0.png",
            "background": f"{server}https://lo1.in/BR/bahia0.png",
            "description": "Canal BR| BAHIA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162392.m3u8",
                    "title": "BR| BAHIA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal6",
            "type": "tv",
            "name": "BR| BAND HD",
            "poster": f"{server}https://lo1.in/BR/band.png",
            "background": f"{server}https://lo1.in/BR/band.png",
            "description": "Canal BR| BAND HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162309.m3u8",
                    "title": "BR| BAND HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal7",
            "type": "tv",
            "name": "BR| BAND NEWS HD",
            "poster": f"{server}https://lo1.in/BR/banns1.png",
            "background": f"{server}https://lo1.in/BR/banns1.png",
            "description": "Canal BR| BAND NEWS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162311.m3u8",
                    "title": "BR| BAND NEWS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal8",
            "type": "tv",
            "name": "BR| BAND SP HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| BAND SP HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37424.m3u8",
                    "title": "BR| BAND SP HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal9",
            "type": "tv",
            "name": "BR| BIS HD",
            "poster": f"{server}https://lo1.in/BR/bis.png",
            "background": f"{server}https://lo1.in/BR/bis.png",
            "description": "Canal BR| BIS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171349.m3u8",
                    "title": "BR| BIS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal10",
            "type": "tv",
            "name": "BR| CANAL BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/cnlbrs.png",
            "background": f"{server}https://lo1.in/BR/cnlbrs.png",
            "description": "Canal BR| CANAL BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162316.m3u8",
                    "title": "BR| CANAL BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal11",
            "type": "tv",
            "name": "BR| COMBATE HD",
            "poster": f"{server}https://lo1.in/BR/combt.png",
            "background": f"{server}https://lo1.in/BR/combt.png",
            "description": "Canal BR| COMBATE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162327.m3u8",
                    "title": "BR| COMBATE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal12",
            "type": "tv",
            "name": "BR| COMEDY CENTRAL HD",
            "poster": f"{server}https://lo1.in/BR/cmdcnt.png",
            "background": f"{server}https://lo1.in/BR/cmdcnt.png",
            "description": "Canal BR| COMEDY CENTRAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162329.m3u8",
                    "title": "BR| COMEDY CENTRAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal13",
            "type": "tv",
            "name": "BR| CURTA! HD",
            "poster": f"{server}https://lo1.in/BR/cl7.png",
            "background": f"{server}https://lo1.in/BR/cl7.png",
            "description": "Canal BR| CURTA! HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162332.m3u8",
                    "title": "BR| CURTA! HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal14",
            "type": "tv",
            "name": "BR| FISH TV HD",
            "poster": f"{server}https://lo1.in/BR/fish.png",
            "background": f"{server}https://lo1.in/BR/fish.png",
            "description": "Canal BR| FISH TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331282.m3u8",
                    "title": "BR| FISH TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal15",
            "type": "tv",
            "name": "BR| TV CIDADE CANAL 9 HD",
            "poster": f"{server}https://lo1.in/BR/cidcnl9.png",
            "background": f"{server}https://lo1.in/BR/cidcnl9.png",
            "description": "Canal BR| TV CIDADE CANAL 9 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380035.m3u8",
                    "title": "BR| TV CIDADE CANAL 9 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal16",
            "type": "tv",
            "name": "BR| FILM & ARTS HD",
            "poster": f"{server}https://lo1.in/arg/fart.png",
            "background": f"{server}https://lo1.in/arg/fart.png",
            "description": "Canal BR| FILM & ARTS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380033.m3u8",
                    "title": "BR| FILM & ARTS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal17",
            "type": "tv",
            "name": "BR| GOSPEL MOVIES TELEVISION HD",
            "poster": f"{server}https://lo1.in/BR/gosmv.png",
            "background": f"{server}https://lo1.in/BR/gosmv.png",
            "description": "Canal BR| GOSPEL MOVIES TELEVISION HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380032.m3u8",
                    "title": "BR| GOSPEL MOVIES TELEVISION HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal18",
            "type": "tv",
            "name": "BR| ITV HD",
            "poster": f"{server}https://lo1.in/BR/itv.png",
            "background": f"{server}https://lo1.in/BR/itv.png",
            "description": "Canal BR| ITV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380031.m3u8",
                    "title": "BR| ITV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal19",
            "type": "tv",
            "name": "BR| PFC HD",
            "poster": f"{server}https://lo1.in/BR/pfc.png",
            "background": f"{server}https://lo1.in/BR/pfc.png",
            "description": "Canal BR| PFC HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380027.m3u8",
                    "title": "BR| PFC HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal20",
            "type": "tv",
            "name": "BR| TV UFSC HD",
            "poster": f"{server}https://lo1.in/BR/ufs.png",
            "background": f"{server}https://lo1.in/BR/ufs.png",
            "description": "Canal BR| TV UFSC HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397465.m3u8",
                    "title": "BR| TV UFSC HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal21",
            "type": "tv",
            "name": "BR| REDE BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/rdet0.png",
            "background": f"{server}https://lo1.in/BR/rdet0.png",
            "description": "Canal BR| REDE BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162489.m3u8",
                    "title": "BR| REDE BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal22",
            "type": "tv",
            "name": "BR| REDE VIDA HD",
            "poster": f"{server}https://lo1.in/BR/rdet0.png",
            "background": f"{server}https://lo1.in/BR/rdet0.png",
            "description": "Canal BR| REDE VIDA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162492.m3u8",
                    "title": "BR| REDE VIDA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal23",
            "type": "tv",
            "name": "BR| REDE TV HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| REDE TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37411.m3u8",
                    "title": "BR| REDE TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal24",
            "type": "tv",
            "name": "BR| REDE FAMILIA HD",
            "poster": f"{server}https://lo1.in/BR/rdfm.png",
            "background": f"{server}https://lo1.in/BR/rdfm.png",
            "description": "Canal BR| REDE FAMILIA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380024.m3u8",
                    "title": "BR| REDE FAMILIA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal25",
            "type": "tv",
            "name": "BR| REDE GOSPEL HD",
            "poster": f"{server}https://lo1.in/BR/rdgsp.png",
            "background": f"{server}https://lo1.in/BR/rdgsp.png",
            "description": "Canal BR| REDE GOSPEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380023.m3u8",
                    "title": "BR| REDE GOSPEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal26",
            "type": "tv",
            "name": "BR| REDE MÃO AMIGA HD",
            "poster": f"{server}https://lo1.in/BR/mao.png",
            "background": f"{server}https://lo1.in/BR/mao.png",
            "description": "Canal BR| REDE MÃO AMIGA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397454.m3u8",
                    "title": "BR| REDE MÃO AMIGA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal27",
            "type": "tv",
            "name": "BR| SPACE HD",
            "poster": f"{server}https://lo1.in/BR/spc.png",
            "background": f"{server}https://lo1.in/BR/spc.png",
            "description": "Canal BR| SPACE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380020.m3u8",
                    "title": "BR| SPACE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal28",
            "type": "tv",
            "name": "BR| TVN BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/tnbr.png",
            "background": f"{server}https://lo1.in/BR/tnbr.png",
            "description": "Canal BR| TVN BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380017.m3u8",
                    "title": "BR| TVN BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal29",
            "type": "tv",
            "name": "BR| GNT HD",
            "poster": f"{server}https://lo1.in/BR/gnt.png",
            "background": f"{server}https://lo1.in/BR/gnt.png",
            "description": "Canal BR| GNT HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331230.m3u8",
                    "title": "BR| GNT HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal30",
            "type": "tv",
            "name": "BR| HGTV HD",
            "poster": f"{server}https://lo1.in/BR/hg.png",
            "background": f"{server}https://lo1.in/BR/hg.png",
            "description": "Canal BR| HGTV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162439.m3u8",
                    "title": "BR| HGTV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal31",
            "type": "tv",
            "name": "BR| MULTISHOW HD",
            "poster": f"{server}https://lo1.in/BR/multsh.png",
            "background": f"{server}https://lo1.in/BR/multsh.png",
            "description": "Canal BR| MULTISHOW HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331257.m3u8",
                    "title": "BR| MULTISHOW HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal32",
            "type": "tv",
            "name": "BR| NOVO TEMPO HD",
            "poster": f"{server}https://lo1.in/BR/novotem.png",
            "background": f"{server}https://lo1.in/BR/novotem.png",
            "description": "Canal BR| NOVO TEMPO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331231.m3u8",
                    "title": "BR| NOVO TEMPO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal33",
            "type": "tv",
            "name": "BR| OFF HD",
            "poster": f"{server}https://lo1.in/BR/off.png",
            "background": f"{server}https://lo1.in/BR/off.png",
            "description": "Canal BR| OFF HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331258.m3u8",
                    "title": "BR| OFF HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal34",
            "type": "tv",
            "name": "BR| RECORD HD",
            "poster": f"{server}https://lo1.in/BR/rcrd.png",
            "background": f"{server}https://lo1.in/BR/rcrd.png",
            "description": "Canal BR| RECORD HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162550.m3u8",
                    "title": "BR| RECORD HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal35",
            "type": "tv",
            "name": "BR| RECORD NEWS HD",
            "poster": f"{server}https://lo1.in/BR/rcord.png",
            "background": f"{server}https://lo1.in/BR/rcord.png",
            "description": "Canal BR| RECORD NEWS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162484.m3u8",
                    "title": "BR| RECORD NEWS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal36",
            "type": "tv",
            "name": "BR| RECORD MG HD",
            "poster": f"{server}https://lo1.in/BR/rcord.png",
            "background": f"{server}https://lo1.in/BR/rcord.png",
            "description": "Canal BR| RECORD MG HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162483.m3u8",
                    "title": "BR| RECORD MG HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal37",
            "type": "tv",
            "name": "BR| RECORD NORDESTE HD",
            "poster": f"{server}https://lo1.in/BR/rcord.png",
            "background": f"{server}https://lo1.in/BR/rcord.png",
            "description": "Canal BR| RECORD NORDESTE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162485.m3u8",
                    "title": "BR| RECORD NORDESTE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal38",
            "type": "tv",
            "name": "BR| RECORD RS HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| RECORD RS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37406.m3u8",
                    "title": "BR| RECORD RS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal39",
            "type": "tv",
            "name": "BR| RECORD RJ HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| RECORD RJ HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37407.m3u8",
                    "title": "BR| RECORD RJ HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal40",
            "type": "tv",
            "name": "BR| RECORD CAMPINAS HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| RECORD CAMPINAS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37410.m3u8",
                    "title": "BR| RECORD CAMPINAS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal41",
            "type": "tv",
            "name": "BR| RECORD BAHIA HD",
            "poster": f"{server}https://lo1.in/BR/rcrd.png",
            "background": f"{server}https://lo1.in/BR/rcrd.png",
            "description": "Canal BR| RECORD BAHIA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/53103.m3u8",
                    "title": "BR| RECORD BAHIA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal42",
            "type": "tv",
            "name": "BR| SBT HD",
            "poster": f"{server}https://lo1.in/BR/sbt.png",
            "background": f"{server}https://lo1.in/BR/sbt.png",
            "description": "Canal BR| SBT HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162495.m3u8",
                    "title": "BR| SBT HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal43",
            "type": "tv",
            "name": "BR| SBT NORDESTE HD",
            "poster": f"{server}https://lo1.in/BR/sbt.png",
            "background": f"{server}https://lo1.in/BR/sbt.png",
            "description": "Canal BR| SBT NORDESTE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162496.m3u8",
                    "title": "BR| SBT NORDESTE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal44",
            "type": "tv",
            "name": "BR| SBT RJ HD",
            "poster": f"{server}https://lo1.in/BR/sbt.png",
            "background": f"{server}https://lo1.in/BR/sbt.png",
            "description": "Canal BR| SBT RJ HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162497.m3u8",
                    "title": "BR| SBT RJ HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal45",
            "type": "tv",
            "name": "BR| SBT SP HD",
            "poster": f"{server}https://lo1.in/BR/sbt.png",
            "background": f"{server}https://lo1.in/BR/sbt.png",
            "description": "Canal BR| SBT SP HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162494.m3u8",
                    "title": "BR| SBT SP HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal46",
            "type": "tv",
            "name": "BR| SONY HD",
            "poster": f"{server}https://lo1.in/BR/sny.png",
            "background": f"{server}https://lo1.in/BR/sny.png",
            "description": "Canal BR| SONY HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162499.m3u8",
                    "title": "BR| SONY HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal47",
            "type": "tv",
            "name": "BR| SYFY HD",
            "poster": f"{server}https://lo1.in/BR/syf.png",
            "background": f"{server}https://lo1.in/BR/syf.png",
            "description": "Canal BR| SYFY HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331259.m3u8",
                    "title": "BR| SYFY HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal48",
            "type": "tv",
            "name": "BR| TBS HD",
            "poster": f"{server}https://lo1.in/BR/tbs.png",
            "background": f"{server}https://lo1.in/BR/tbs.png",
            "description": "Canal BR| TBS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331260.m3u8",
                    "title": "BR| TBS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal49",
            "type": "tv",
            "name": "BR| TCM HD",
            "poster": f"{server}https://lo1.in/BR/tcm.png",
            "background": f"{server}https://lo1.in/BR/tcm.png",
            "description": "Canal BR| TCM HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162509.m3u8",
                    "title": "BR| TCM HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal50",
            "type": "tv",
            "name": "BR| TNT HD",
            "poster": f"{server}https://lo1.in/BR/tnt.png",
            "background": f"{server}https://lo1.in/BR/tnt.png",
            "description": "Canal BR| TNT HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171329.m3u8",
                    "title": "BR| TNT HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal51",
            "type": "tv",
            "name": "BR| TV DIARIO HD",
            "poster": f"{server}https://lo1.in/BR/diar.png",
            "background": f"{server}https://lo1.in/BR/diar.png",
            "description": "Canal BR| TV DIARIO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162535.m3u8",
                    "title": "BR| TV DIARIO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal52",
            "type": "tv",
            "name": "BR| TV GAZETA HD",
            "poster": f"{server}https://lo1.in/BR/tgaze.png",
            "background": f"{server}https://lo1.in/BR/tgaze.png",
            "description": "Canal BR| TV GAZETA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171348.m3u8",
                    "title": "BR| TV GAZETA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal53",
            "type": "tv",
            "name": "BR| TV TEM BAURU HD",
            "poster": f"{server}https://lo1.in/BR/ttem.png",
            "background": f"{server}https://lo1.in/BR/ttem.png",
            "description": "Canal BR| TV TEM BAURU HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331237.m3u8",
                    "title": "BR| TV TEM BAURU HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal54",
            "type": "tv",
            "name": "BR| TV TEM SOROCABA HD",
            "poster": f"{server}https://lo1.in/BR/ttem.png",
            "background": f"{server}https://lo1.in/BR/ttem.png",
            "description": "Canal BR| TV TEM SOROCABA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162423.m3u8",
                    "title": "BR| TV TEM SOROCABA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal55",
            "type": "tv",
            "name": "BR| TV TRIBUNA SANTOS HD",
            "poster": f"{server}https://lo1.in/BR/ttrib.png",
            "background": f"{server}https://lo1.in/BR/ttrib.png",
            "description": "Canal BR| TV TRIBUNA SANTOS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162424.m3u8",
                    "title": "BR| TV TRIBUNA SANTOS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal56",
            "type": "tv",
            "name": "BR| UNIVERSAL CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/univch.png",
            "background": f"{server}https://lo1.in/BR/univch.png",
            "description": "Canal BR| UNIVERSAL CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162552.m3u8",
                    "title": "BR| UNIVERSAL CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal57",
            "type": "tv",
            "name": "BR| TV VANGUARDA DOS CAMPOS HD",
            "poster": f"{server}https://lo1.in/BR/tangu.png",
            "background": f"{server}https://lo1.in/BR/tangu.png",
            "description": "Canal BR| TV VANGUARDA DOS CAMPOS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331239.m3u8",
                    "title": "BR| TV VANGUARDA DOS CAMPOS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal58",
            "type": "tv",
            "name": "BR| TV VERDES MARES FORTALEZA HD",
            "poster": f"{server}https://lo1.in/BR/terdes.png",
            "background": f"{server}https://lo1.in/BR/terdes.png",
            "description": "Canal BR| TV VERDES MARES FORTALEZA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162426.m3u8",
                    "title": "BR| TV VERDES MARES FORTALEZA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal59",
            "type": "tv",
            "name": "BR| VIVA HD",
            "poster": f"{server}https://lo1.in/BR/vivah.png",
            "background": f"{server}https://lo1.in/BR/vivah.png",
            "description": "Canal BR| VIVA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331228.m3u8",
                    "title": "BR| VIVA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal60",
            "type": "tv",
            "name": "BR| WARNER CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/warnch.png",
            "background": f"{server}https://lo1.in/BR/warnch.png",
            "description": "Canal BR| WARNER CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331251.m3u8",
                    "title": "BR| WARNER CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal61",
            "type": "tv",
            "name": "BR| WOOHOO HD",
            "poster": f"{server}https://lo1.in/BR/woho.png",
            "background": f"{server}https://lo1.in/BR/woho.png",
            "description": "Canal BR| WOOHOO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162563.m3u8",
                    "title": "BR| WOOHOO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal62",
            "type": "tv",
            "name": "BR| ZOOMOO HD",
            "poster": f"{server}https://lo1.in/BR/zomo.png",
            "background": f"{server}https://lo1.in/BR/zomo.png",
            "description": "Canal BR| ZOOMOO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162565.m3u8",
                    "title": "BR| ZOOMOO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal63",
            "type": "tv",
            "name": "BR| SANTA CECILIA TV HD",
            "poster": f"{server}https://lo1.in/BR/santa.png",
            "background": f"{server}https://lo1.in/BR/santa.png",
            "description": "Canal BR| SANTA CECILIA TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397450.m3u8",
                    "title": "BR| SANTA CECILIA TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal64",
            "type": "tv",
            "name": "BR| TERRA VIVA HD",
            "poster": f"{server}https://lo1.in/BR/tervi.png",
            "background": f"{server}https://lo1.in/BR/tervi.png",
            "description": "Canal BR| TERRA VIVA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397449.m3u8",
                    "title": "BR| TERRA VIVA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal65",
            "type": "tv",
            "name": "BR| TV CINEC SD",
            "poster": f"{server}https://lo1.in/BR/cine.png",
            "background": f"{server}https://lo1.in/BR/cine.png",
            "description": "Canal BR| TV CINEC SD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397444.m3u8",
                    "title": "BR| TV CINEC SD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal66",
            "type": "tv",
            "name": "BR| TV DESTAK SD",
            "poster": f"{server}https://lo1.in/BR/destak1.png",
            "background": f"{server}https://lo1.in/BR/destak1.png",
            "description": "Canal BR| TV DESTAK SD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397442.m3u8",
                    "title": "BR| TV DESTAK SD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal67",
            "type": "tv",
            "name": "BR| TV DIGITAL BIRIGUI HD",
            "poster": f"{server}https://lo1.in/BR/digit.png",
            "background": f"{server}https://lo1.in/BR/digit.png",
            "description": "Canal BR| TV DIGITAL BIRIGUI HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397441.m3u8",
                    "title": "BR| TV DIGITAL BIRIGUI HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal68",
            "type": "tv",
            "name": "BR| TV GALEGA HD",
            "poster": f"{server}https://lo1.in/BR/galg.png",
            "background": f"{server}https://lo1.in/BR/galg.png",
            "description": "Canal BR| TV GALEGA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397440.m3u8",
                    "title": "BR| TV GALEGA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal69",
            "type": "tv",
            "name": "BR| TV METRÓPOLE HD",
            "poster": f"{server}https://lo1.in/BR/metro.png",
            "background": f"{server}https://lo1.in/BR/metro.png",
            "description": "Canal BR| TV METRÓPOLE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397436.m3u8",
                    "title": "BR| TV METRÓPOLE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal70",
            "type": "tv",
            "name": "BR| TV PAI ETERNO HD",
            "poster": f"{server}https://lo1.in/BR/tpai.png",
            "background": f"{server}https://lo1.in/BR/tpai.png",
            "description": "Canal BR| TV PAI ETERNO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397435.m3u8",
                    "title": "BR| TV PAI ETERNO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal71",
            "type": "tv",
            "name": "BR| TV SOL COMUNIDADE HD",
            "poster": f"{server}https://lo1.in/BR/tsolcom.png",
            "background": f"{server}https://lo1.in/BR/tsolcom.png",
            "description": "Canal BR| TV SOL COMUNIDADE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397433.m3u8",
                    "title": "BR| TV SOL COMUNIDADE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal72",
            "type": "tv",
            "name": "BR| TV TERCEIRO ANJO HD",
            "poster": f"{server}https://lo1.in/BR/tterc.png",
            "background": f"{server}https://lo1.in/BR/tterc.png",
            "description": "Canal BR| TV TERCEIRO ANJO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397432.m3u8",
                    "title": "BR| TV TERCEIRO ANJO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal73",
            "type": "tv",
            "name": "BR| UNITV PORTO ALEGRE HD",
            "poster": f"{server}https://lo1.in/BR/unitaleg.png",
            "background": f"{server}https://lo1.in/BR/unitaleg.png",
            "description": "Canal BR| UNITV PORTO ALEGRE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397426.m3u8",
                    "title": "BR| UNITV PORTO ALEGRE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal74",
            "type": "tv",
            "name": "BR| TV CAMARA HD",
            "poster": f"{server}https://lo1.in/BR/camr.png",
            "background": f"{server}https://lo1.in/BR/camr.png",
            "description": "Canal BR| TV CAMARA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331234.m3u8",
                    "title": "BR| TV CAMARA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal75",
            "type": "tv",
            "name": "BR| TV BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| TV BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37403.m3u8",
                    "title": "BR| TV BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal76",
            "type": "tv",
            "name": "BR| BBB CAM 01 (ACOMPANHE A CASA 1)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 01 (ACOMPANHE A CASA 1) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562219.m3u8",
                    "title": "BR| BBB CAM 01 (ACOMPANHE A CASA 1)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal77",
            "type": "tv",
            "name": "BR| BBB CAM 02 (ACOMPANHE A CASA 2)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 02 (ACOMPANHE A CASA 2) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562220.m3u8",
                    "title": "BR| BBB CAM 02 (ACOMPANHE A CASA 2)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal78",
            "type": "tv",
            "name": "BR| BBB CAM 03 (MOSAICO)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 03 (MOSAICO) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562221.m3u8",
                    "title": "BR| BBB CAM 03 (MOSAICO)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal79",
            "type": "tv",
            "name": "BR| BBB CAM 04 (COZINHA)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 04 (COZINHA) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562222.m3u8",
                    "title": "BR| BBB CAM 04 (COZINHA)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal80",
            "type": "tv",
            "name": "BR| BBB CAM 05 (QUARTO ANOS 50)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 05 (QUARTO ANOS 50) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562223.m3u8",
                    "title": "BR| BBB CAM 05 (QUARTO ANOS 50)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal81",
            "type": "tv",
            "name": "BR| BBB CAM 06 (QUARTO NORDESTE)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 06 (QUARTO NORDESTE) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562224.m3u8",
                    "title": "BR| BBB CAM 06 (QUARTO NORDESTE)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal82",
            "type": "tv",
            "name": "BR| BBB CAM 07 (QUARTO FANTÁSTICO)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 07 (QUARTO FANTÁSTICO) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562225.m3u8",
                    "title": "BR| BBB CAM 07 (QUARTO FANTÁSTICO)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal83",
            "type": "tv",
            "name": "BR| BBB CAM 08 (COZINHA 2)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 08 (COZINHA 2) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562226.m3u8",
                    "title": "BR| BBB CAM 08 (COZINHA 2)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal84",
            "type": "tv",
            "name": "BR| BBB CAM 09 (CÂMERA PANTENE)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 09 (CÂMERA PANTENE) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562227.m3u8",
                    "title": "BR| BBB CAM 09 (CÂMERA PANTENE)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal85",
            "type": "tv",
            "name": "BR| BBB CAM 10 (SALA)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 10 (SALA) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562228.m3u8",
                    "title": "BR| BBB CAM 10 (SALA)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal86",
            "type": "tv",
            "name": "BR| BBB CAM 11 (PISCINA)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 11 (PISCINA) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401562229.m3u8",
                    "title": "BR| BBB CAM 11 (PISCINA)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal87",
            "type": "tv",
            "name": "BR| BBB CAM 12 (ACADEMIA)",
            "poster": f"{server}https://lo1.in/BR/bigbrz.png",
            "background": f"{server}https://lo1.in/BR/bigbrz.png",
            "description": "Canal BR| BBB CAM 12 (ACADEMIA) ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/401564167.m3u8",
                    "title": "BR| BBB CAM 12 (ACADEMIA)",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal88",
            "type": "tv",
            "name": "✦●✦ SPORTS✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ SPORTS✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355446.m3u8",
                    "title": "✦●✦ SPORTS✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal89",
            "type": "tv",
            "name": "BR| 100 AUTO MOTO TV SD",
            "poster": f"{server}https://lo1.in/BR/10atmt1.png",
            "background": f"{server}https://lo1.in/BR/10atmt1.png",
            "description": "Canal BR| 100 AUTO MOTO TV SD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162296.m3u8",
                    "title": "BR| 100 AUTO MOTO TV SD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal90",
            "type": "tv",
            "name": "BR| ALL SPORTS HD",
            "poster": f"{server}https://lo1.in/BR/alsp.png",
            "background": f"{server}https://lo1.in/BR/alsp.png",
            "description": "Canal BR| ALL SPORTS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162302.m3u8",
                    "title": "BR| ALL SPORTS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal91",
            "type": "tv",
            "name": "BR| BAND SPORTS HD",
            "poster": f"{server}https://lo1.in/BR/bansp.png",
            "background": f"{server}https://lo1.in/BR/bansp.png",
            "description": "Canal BR| BAND SPORTS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162313.m3u8",
                    "title": "BR| BAND SPORTS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal92",
            "type": "tv",
            "name": "BR| CONMEBOL TV  1 HD",
            "poster": f"{server}https://lo1.in/BR/conmbl.png",
            "background": f"{server}https://lo1.in/BR/conmbl.png",
            "description": "Canal BR| CONMEBOL TV  1 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/360178.m3u8",
                    "title": "BR| CONMEBOL TV  1 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal93",
            "type": "tv",
            "name": "BR| CONMEBOL TV 2 HD",
            "poster": f"{server}https://lo1.in/BR/conmbl.png",
            "background": f"{server}https://lo1.in/BR/conmbl.png",
            "description": "Canal BR| CONMEBOL TV 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/360179.m3u8",
                    "title": "BR| CONMEBOL TV 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal94",
            "type": "tv",
            "name": "BR| CONMEBOL TV  3 HD",
            "poster": f"{server}https://lo1.in/BR/conmbl.png",
            "background": f"{server}https://lo1.in/BR/conmbl.png",
            "description": "Canal BR| CONMEBOL TV  3 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/379635.m3u8",
                    "title": "BR| CONMEBOL TV  3 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal95",
            "type": "tv",
            "name": "BR| CONMEBOL TV 4 HD",
            "poster": f"{server}https://lo1.in/BR/conmbl.png",
            "background": f"{server}https://lo1.in/BR/conmbl.png",
            "description": "Canal BR| CONMEBOL TV 4 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/379636.m3u8",
                    "title": "BR| CONMEBOL TV 4 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal96",
            "type": "tv",
            "name": "BR| ESPN BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/espbrs.png",
            "background": f"{server}https://lo1.in/BR/espbrs.png",
            "description": "Canal BR| ESPN BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162359.m3u8",
                    "title": "BR| ESPN BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal97",
            "type": "tv",
            "name": "BR| ESPN EXTRA HD",
            "poster": f"{server}https://lo1.in/BR/esp.png",
            "background": f"{server}https://lo1.in/BR/esp.png",
            "description": "Canal BR| ESPN EXTRA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171310.m3u8",
                    "title": "BR| ESPN EXTRA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal98",
            "type": "tv",
            "name": "BR| ESPN HD",
            "poster": f"{server}https://lo1.in/BR/espex.png",
            "background": f"{server}https://lo1.in/BR/espex.png",
            "description": "Canal BR| ESPN HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171302.m3u8",
                    "title": "BR| ESPN HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal99",
            "type": "tv",
            "name": "BR| ESPN 2 HD",
            "poster": f"{server}https://lo1.in/BR/esp.png",
            "background": f"{server}https://lo1.in/BR/esp.png",
            "description": "Canal BR| ESPN 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171301.m3u8",
                    "title": "BR| ESPN 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal100",
            "type": "tv",
            "name": "BR| ESPN 3 HD",
            "poster": f"{server}https://lo1.in/BR/espex.png",
            "background": f"{server}https://lo1.in/BR/espex.png",
            "description": "Canal BR| ESPN 3 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162360.m3u8",
                    "title": "BR| ESPN 3 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal101",
            "type": "tv",
            "name": "BR| ESPN 4 HD",
            "poster": f"{server}https://lo1.in/BR/espn4.png",
            "background": f"{server}https://lo1.in/BR/espn4.png",
            "description": "Canal BR| ESPN 4 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162358.m3u8",
                    "title": "BR| ESPN 4 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal102",
            "type": "tv",
            "name": "BR| FOX SPORTS 2 HD",
            "poster": f"{server}https://lo1.in/BR/fxsp.png",
            "background": f"{server}https://lo1.in/BR/fxsp.png",
            "description": "Canal BR| FOX SPORTS 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162381.m3u8",
                    "title": "BR| FOX SPORTS 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal103",
            "type": "tv",
            "name": "BR| FOX SPORTS HD",
            "poster": f"{server}https://lo1.in/BR/fxsp.png",
            "background": f"{server}https://lo1.in/BR/fxsp.png",
            "description": "Canal BR| FOX SPORTS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162380.m3u8",
                    "title": "BR| FOX SPORTS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal104",
            "type": "tv",
            "name": "BR| SPORTV 1 HD",
            "poster": f"{server}https://lo1.in/BR/sp1.png",
            "background": f"{server}https://lo1.in/BR/sp1.png",
            "description": "Canal BR| SPORTV 1 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171307.m3u8",
                    "title": "BR| SPORTV 1 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal105",
            "type": "tv",
            "name": "BR| SPORTV 2 HD",
            "poster": f"{server}https://lo1.in/BR/spt2.png",
            "background": f"{server}https://lo1.in/BR/spt2.png",
            "description": "Canal BR| SPORTV 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171308.m3u8",
                    "title": "BR| SPORTV 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal106",
            "type": "tv",
            "name": "BR| SPORTV 3 HD",
            "poster": f"{server}https://lo1.in/BR/spt3.png",
            "background": f"{server}https://lo1.in/BR/spt3.png",
            "description": "Canal BR| SPORTV 3 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171309.m3u8",
                    "title": "BR| SPORTV 3 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal107",
            "type": "tv",
            "name": "BR| PARAMOUNT CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/paramch.png",
            "background": f"{server}https://lo1.in/BR/paramch.png",
            "description": "Canal BR| PARAMOUNT CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162465.m3u8",
                    "title": "BR| PARAMOUNT CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal108",
            "type": "tv",
            "name": "BR| PREMIERE 1 HD",
            "poster": f"{server}https://lo1.in/BR/prme.png",
            "background": f"{server}https://lo1.in/BR/prme.png",
            "description": "Canal BR| PREMIERE 1 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162468.m3u8",
                    "title": "BR| PREMIERE 1 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal109",
            "type": "tv",
            "name": "BR| PREMIERE 2 HD",
            "poster": f"{server}https://lo1.in/BR/prme2.png",
            "background": f"{server}https://lo1.in/BR/prme2.png",
            "description": "Canal BR| PREMIERE 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331246.m3u8",
                    "title": "BR| PREMIERE 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal110",
            "type": "tv",
            "name": "BR| PREMIERE 3 HD",
            "poster": f"{server}https://lo1.in/BR/prme3.png",
            "background": f"{server}https://lo1.in/BR/prme3.png",
            "description": "Canal BR| PREMIERE 3 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331247.m3u8",
                    "title": "BR| PREMIERE 3 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal111",
            "type": "tv",
            "name": "BR| PREMIERE 4 HD",
            "poster": f"{server}https://lo1.in/BR/prme.png",
            "background": f"{server}https://lo1.in/BR/prme.png",
            "description": "Canal BR| PREMIERE 4 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162471.m3u8",
                    "title": "BR| PREMIERE 4 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal112",
            "type": "tv",
            "name": "BR| PREMIERE 5 HD",
            "poster": f"{server}https://lo1.in/BR/prme.png",
            "background": f"{server}https://lo1.in/BR/prme.png",
            "description": "Canal BR| PREMIERE 5 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331248.m3u8",
                    "title": "BR| PREMIERE 5 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal113",
            "type": "tv",
            "name": "BR| PREMIERE 6 HD",
            "poster": f"{server}https://lo1.in/BR/prme.png",
            "background": f"{server}https://lo1.in/BR/prme.png",
            "description": "Canal BR| PREMIERE 6 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331249.m3u8",
                    "title": "BR| PREMIERE 6 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal114",
            "type": "tv",
            "name": "BR| PREMIERE 7 HD",
            "poster": f"{server}https://lo1.in/BR/prme7.png",
            "background": f"{server}https://lo1.in/BR/prme7.png",
            "description": "Canal BR| PREMIERE 7 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/400230122.m3u8",
                    "title": "BR| PREMIERE 7 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal115",
            "type": "tv",
            "name": "✦●✦ CINEMA✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ CINEMA✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355445.m3u8",
                    "title": "✦●✦ CINEMA✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal116",
            "type": "tv",
            "name": "BR| AXN HD",
            "poster": f"{server}https://lo1.in/BR/axn.png",
            "background": f"{server}https://lo1.in/BR/axn.png",
            "description": "Canal BR| AXN HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171323.m3u8",
                    "title": "BR| AXN HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal117",
            "type": "tv",
            "name": "BR| CINEMAX HD",
            "poster": f"{server}https://lo1.in/BR/cinmx.png",
            "background": f"{server}https://lo1.in/BR/cinmx.png",
            "description": "Canal BR| CINEMAX HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171327.m3u8",
                    "title": "BR| CINEMAX HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal118",
            "type": "tv",
            "name": "BR| MEGAPIX HD",
            "poster": f"{server}https://lo1.in/BR/megapx.png",
            "background": f"{server}https://lo1.in/BR/megapx.png",
            "description": "Canal BR| MEGAPIX HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171297.m3u8",
                    "title": "BR| MEGAPIX HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal119",
            "type": "tv",
            "name": "BR| FOX HD",
            "poster": f"{server}https://lo1.in/BR/fox.png",
            "background": f"{server}https://lo1.in/BR/fox.png",
            "description": "Canal BR| FOX HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162384.m3u8",
                    "title": "BR| FOX HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal120",
            "type": "tv",
            "name": "BR| FX HD",
            "poster": f"{server}https://lo1.in/BR/fx.png",
            "background": f"{server}https://lo1.in/BR/fx.png",
            "description": "Canal BR| FX HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331254.m3u8",
                    "title": "BR| FX HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal121",
            "type": "tv",
            "name": "BR| HBO HD",
            "poster": f"{server}https://lo1.in/BR/hbo.png",
            "background": f"{server}https://lo1.in/BR/hbo.png",
            "description": "Canal BR| HBO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171313.m3u8",
                    "title": "BR| HBO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal122",
            "type": "tv",
            "name": "BR| HBO 2 HD",
            "poster": f"{server}https://lo1.in/BR/hbo2.png",
            "background": f"{server}https://lo1.in/BR/hbo2.png",
            "description": "Canal BR| HBO 2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171314.m3u8",
                    "title": "BR| HBO 2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal123",
            "type": "tv",
            "name": "BR| HBO FAMILY HD",
            "poster": f"{server}https://lo1.in/BR/hbofm.png",
            "background": f"{server}https://lo1.in/BR/hbofm.png",
            "description": "Canal BR| HBO FAMILY HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331242.m3u8",
                    "title": "BR| HBO FAMILY HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal124",
            "type": "tv",
            "name": "BR| HBO MUNDI HD",
            "poster": f"{server}https://lo1.in/BR/hbom.png",
            "background": f"{server}https://lo1.in/BR/hbom.png",
            "description": "Canal BR| HBO MUNDI HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331244.m3u8",
                    "title": "BR| HBO MUNDI HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal125",
            "type": "tv",
            "name": "BR| HBO PLUS HD",
            "poster": f"{server}https://lo1.in/BR/hbopl.png",
            "background": f"{server}https://lo1.in/BR/hbopl.png",
            "description": "Canal BR| HBO PLUS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171315.m3u8",
                    "title": "BR| HBO PLUS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal126",
            "type": "tv",
            "name": "BR| HBO POP HD",
            "poster": f"{server}https://lo1.in/BR/hbopo.png",
            "background": f"{server}https://lo1.in/BR/hbopo.png",
            "description": "Canal BR| HBO POP HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331245.m3u8",
                    "title": "BR| HBO POP HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal127",
            "type": "tv",
            "name": "BR| HBO SIGNATURE HD",
            "poster": f"{server}https://lo1.in/BR/hbosignat.png",
            "background": f"{server}https://lo1.in/BR/hbosignat.png",
            "description": "Canal BR| HBO SIGNATURE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171333.m3u8",
                    "title": "BR| HBO SIGNATURE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal128",
            "type": "tv",
            "name": "BR| HBO XTREME HD",
            "poster": f"{server}https://lo1.in/BR/hboxtr.png",
            "background": f"{server}https://lo1.in/BR/hboxtr.png",
            "description": "Canal BR| HBO XTREME HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331243.m3u8",
                    "title": "BR| HBO XTREME HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal129",
            "type": "tv",
            "name": "BR| TELECINE ACTION HD",
            "poster": f"{server}https://lo1.in/BR/telact.png",
            "background": f"{server}https://lo1.in/BR/telact.png",
            "description": "Canal BR| TELECINE ACTION HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171316.m3u8",
                    "title": "BR| TELECINE ACTION HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal130",
            "type": "tv",
            "name": "BR| TELECINE CULT HD",
            "poster": f"{server}https://lo1.in/BR/telcu.png",
            "background": f"{server}https://lo1.in/BR/telcu.png",
            "description": "Canal BR| TELECINE CULT HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171332.m3u8",
                    "title": "BR| TELECINE CULT HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal131",
            "type": "tv",
            "name": "BR| TELECINE FUN HD",
            "poster": f"{server}https://lo1.in/BR/telcef.png",
            "background": f"{server}https://lo1.in/BR/telcef.png",
            "description": "Canal BR| TELECINE FUN HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171317.m3u8",
                    "title": "BR| TELECINE FUN HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal132",
            "type": "tv",
            "name": "BR| TELECINE PIPOCA HD",
            "poster": f"{server}https://lo1.in/BR/telpipo.png",
            "background": f"{server}https://lo1.in/BR/telpipo.png",
            "description": "Canal BR| TELECINE PIPOCA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171318.m3u8",
                    "title": "BR| TELECINE PIPOCA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal133",
            "type": "tv",
            "name": "BR| TELECINE PREMIUM HD",
            "poster": f"{server}https://lo1.in/BR/telcnpr.png",
            "background": f"{server}https://lo1.in/BR/telcnpr.png",
            "description": "Canal BR| TELECINE PREMIUM HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171319.m3u8",
                    "title": "BR| TELECINE PREMIUM HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal134",
            "type": "tv",
            "name": "BR| TELECINE TOUCH HD",
            "poster": f"{server}https://lo1.in/BR/telcnto.png",
            "background": f"{server}https://lo1.in/BR/telcnto.png",
            "description": "Canal BR| TELECINE TOUCH HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171320.m3u8",
                    "title": "BR| TELECINE TOUCH HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal135",
            "type": "tv",
            "name": "BR| TNT SERIES HD",
            "poster": f"{server}https://lo1.in/BR/tntser.png",
            "background": f"{server}https://lo1.in/BR/tntser.png",
            "description": "Canal BR| TNT SERIES HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171322.m3u8",
                    "title": "BR| TNT SERIES HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal136",
            "type": "tv",
            "name": "BR| CINE CANAL HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| CINE CANAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37413.m3u8",
                    "title": "BR| CINE CANAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal137",
            "type": "tv",
            "name": "BR| STAR CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| STAR CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37414.m3u8",
                    "title": "BR| STAR CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal138",
            "type": "tv",
            "name": "✦●✦ DOCUMANTARY✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ DOCUMANTARY✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355448.m3u8",
                    "title": "✦●✦ DOCUMANTARY✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal139",
            "type": "tv",
            "name": "BR| A&E HD",
            "poster": f"{server}https://lo1.in/BR/ane.png",
            "background": f"{server}https://lo1.in/BR/ane.png",
            "description": "Canal BR| A&E HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171324.m3u8",
                    "title": "BR| A&E HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal140",
            "type": "tv",
            "name": "BR| DISCOVERY CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/disch.png",
            "background": f"{server}https://lo1.in/BR/disch.png",
            "description": "Canal BR| DISCOVERY CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171335.m3u8",
                    "title": "BR| DISCOVERY CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal141",
            "type": "tv",
            "name": "BR| DISCOVERY H&H HD",
            "poster": f"{server}https://lo1.in/arg/hhh.png",
            "background": f"{server}https://lo1.in/arg/hhh.png",
            "description": "Canal BR| DISCOVERY H&H HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162341.m3u8",
                    "title": "BR| DISCOVERY H&H HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal142",
            "type": "tv",
            "name": "BR| DISCOVERY ID-INVESTIGACAO HD",
            "poster": f"{server}https://lo1.in/BR/disinve.png",
            "background": f"{server}https://lo1.in/BR/disinve.png",
            "description": "Canal BR| DISCOVERY ID-INVESTIGACAO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162443.m3u8",
                    "title": "BR| DISCOVERY ID-INVESTIGACAO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal143",
            "type": "tv",
            "name": "BR| DISCOVERY KIDS HD",
            "poster": f"{server}https://lo1.in/BR/diskds.png",
            "background": f"{server}https://lo1.in/BR/diskds.png",
            "description": "Canal BR| DISCOVERY KIDS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171339.m3u8",
                    "title": "BR| DISCOVERY KIDS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal144",
            "type": "tv",
            "name": "BR| DISCOVERY SCIENCE HD",
            "poster": f"{server}https://lo1.in/BR/dissci.png",
            "background": f"{server}https://lo1.in/BR/dissci.png",
            "description": "Canal BR| DISCOVERY SCIENCE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162344.m3u8",
                    "title": "BR| DISCOVERY SCIENCE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal145",
            "type": "tv",
            "name": "BR| DISCOVERY THEATER HD",
            "poster": f"{server}https://lo1.in/BR/disthe.png",
            "background": f"{server}https://lo1.in/BR/disthe.png",
            "description": "Canal BR| DISCOVERY THEATER HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171336.m3u8",
                    "title": "BR| DISCOVERY THEATER HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal146",
            "type": "tv",
            "name": "BR| DISCOVERY TLC HD",
            "poster": f"{server}https://lo1.in/BR/distlc.png",
            "background": f"{server}https://lo1.in/BR/distlc.png",
            "description": "Canal BR| DISCOVERY TLC HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162346.m3u8",
                    "title": "BR| DISCOVERY TLC HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal147",
            "type": "tv",
            "name": "BR| DISCOVERY TURBO HD",
            "poster": f"{server}https://lo1.in/BR/distrb.png",
            "background": f"{server}https://lo1.in/BR/distrb.png",
            "description": "Canal BR| DISCOVERY TURBO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171334.m3u8",
                    "title": "BR| DISCOVERY TURBO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal148",
            "type": "tv",
            "name": "BR| DISCOVERY WORLD HD",
            "poster": f"{server}https://lo1.in/BR/diswrd.png",
            "background": f"{server}https://lo1.in/BR/diswrd.png",
            "description": "Canal BR| DISCOVERY WORLD HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171337.m3u8",
                    "title": "BR| DISCOVERY WORLD HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal149",
            "type": "tv",
            "name": "BR| FOOD NETWORK HD",
            "poster": f"{server}https://lo1.in/BR/fodnet.png",
            "background": f"{server}https://lo1.in/BR/fodnet.png",
            "description": "Canal BR| FOOD NETWORK HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171345.m3u8",
                    "title": "BR| FOOD NETWORK HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal150",
            "type": "tv",
            "name": "BR| FUTURA HD",
            "poster": f"{server}https://lo1.in/BR/futr.png",
            "background": f"{server}https://lo1.in/BR/futr.png",
            "description": "Canal BR| FUTURA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162386.m3u8",
                    "title": "BR| FUTURA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal151",
            "type": "tv",
            "name": "BR| H2 HD",
            "poster": f"{server}https://lo1.in/BR/h2.png",
            "background": f"{server}https://lo1.in/BR/h2.png",
            "description": "Canal BR| H2 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162432.m3u8",
                    "title": "BR| H2 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal152",
            "type": "tv",
            "name": "BR| HISTORY CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/histch.png",
            "background": f"{server}https://lo1.in/BR/histch.png",
            "description": "Canal BR| HISTORY CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162440.m3u8",
                    "title": "BR| HISTORY CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal153",
            "type": "tv",
            "name": "BR| NAT GEO HD",
            "poster": f"{server}https://lo1.in/BR/natgeo.png",
            "background": f"{server}https://lo1.in/BR/natgeo.png",
            "description": "Canal BR| NAT GEO HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331280.m3u8",
                    "title": "BR| NAT GEO HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal154",
            "type": "tv",
            "name": "BR| NAT GEO KIDS HD",
            "poster": f"{server}https://lo1.in/BR/natgeok.png",
            "background": f"{server}https://lo1.in/BR/natgeok.png",
            "description": "Canal BR| NAT GEO KIDS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171342.m3u8",
                    "title": "BR| NAT GEO KIDS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal155",
            "type": "tv",
            "name": "BR| STUDIO UNIVERSAL HD",
            "poster": f"{server}https://lo1.in/BR/STUDIO UNIVERSAL.png",
            "background": f"{server}https://lo1.in/BR/STUDIO UNIVERSAL.png",
            "description": "Canal BR| STUDIO UNIVERSAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162551.m3u8",
                    "title": "BR| STUDIO UNIVERSAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal156",
            "type": "tv",
            "name": "BR| TRAVEL BOX HD",
            "poster": f"{server}https://lo1.in/BR/trvbx.png",
            "background": f"{server}https://lo1.in/BR/trvbx.png",
            "description": "Canal BR| TRAVEL BOX HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162523.m3u8",
                    "title": "BR| TRAVEL BOX HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal157",
            "type": "tv",
            "name": "BR| ANIMAL PLANET HD",
            "poster": f"{server}https://lo1.in/BR/anmpl.png",
            "background": f"{server}https://lo1.in/BR/anmpl.png",
            "description": "Canal BR| ANIMAL PLANET HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331279.m3u8",
                    "title": "BR| ANIMAL PLANET HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal158",
            "type": "tv",
            "name": "BR| E! HD",
            "poster": f"{server}https://lo1.in/BR/e.png",
            "background": f"{server}https://lo1.in/BR/e.png",
            "description": "Canal BR| E! HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162354.m3u8",
                    "title": "BR| E! HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal159",
            "type": "tv",
            "name": "BR| TV CULTURA HD",
            "poster": f"{server}https://lo1.in/BR/cultr.png",
            "background": f"{server}https://lo1.in/BR/cultr.png",
            "description": "Canal BR| TV CULTURA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162534.m3u8",
                    "title": "BR| TV CULTURA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal160",
            "type": "tv",
            "name": "✦●✦ KIDS✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ KIDS✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355444.m3u8",
                    "title": "✦●✦ KIDS✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal161",
            "type": "tv",
            "name": "BR| BABY TV HD",
            "poster": f"{server}https://lo1.in/BR/bby.png",
            "background": f"{server}https://lo1.in/BR/bby.png",
            "description": "Canal BR| BABY TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162308.m3u8",
                    "title": "BR| BABY TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal162",
            "type": "tv",
            "name": "BR| BOOMERANG HD",
            "poster": f"{server}https://lo1.in/BR/bomer.png",
            "background": f"{server}https://lo1.in/BR/bomer.png",
            "description": "Canal BR| BOOMERANG HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162315.m3u8",
                    "title": "BR| BOOMERANG HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal163",
            "type": "tv",
            "name": "BR| CARTOON NETWORK HD",
            "poster": f"{server}https://lo1.in/BR/crtnet.png",
            "background": f"{server}https://lo1.in/BR/crtnet.png",
            "description": "Canal BR| CARTOON NETWORK HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162321.m3u8",
                    "title": "BR| CARTOON NETWORK HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal164",
            "type": "tv",
            "name": "BR| DISNEY CHANNEL HD",
            "poster": f"{server}https://lo1.in/BR/dsych.png",
            "background": f"{server}https://lo1.in/BR/dsych.png",
            "description": "Canal BR| DISNEY CHANNEL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171338.m3u8",
                    "title": "BR| DISNEY CHANNEL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal165",
            "type": "tv",
            "name": "BR| DISNEY JR HD",
            "poster": f"{server}https://lo1.in/BR/nickjr.png",
            "background": f"{server}https://lo1.in/BR/nickjr.png",
            "description": "Canal BR| DISNEY JR HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171340.m3u8",
                    "title": "BR| DISNEY JR HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal166",
            "type": "tv",
            "name": "BR| DISNEY XD HD",
            "poster": f"{server}https://lo1.in/BR/disxd.png",
            "background": f"{server}https://lo1.in/BR/disxd.png",
            "description": "Canal BR| DISNEY XD HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171343.m3u8",
                    "title": "BR| DISNEY XD HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal167",
            "type": "tv",
            "name": "BR| LIFETIME HD",
            "poster": f"{server}https://lo1.in/BR/lftm.png",
            "background": f"{server}https://lo1.in/BR/lftm.png",
            "description": "Canal BR| LIFETIME HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331229.m3u8",
                    "title": "BR| LIFETIME HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal168",
            "type": "tv",
            "name": "BR| NICK JR HD",
            "poster": f"{server}https://lo1.in/BR/nickjr.png",
            "background": f"{server}https://lo1.in/BR/nickjr.png",
            "description": "Canal BR| NICK JR HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171341.m3u8",
                    "title": "BR| NICK JR HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal169",
            "type": "tv",
            "name": "BR| NICKELODEON HD",
            "poster": f"{server}https://lo1.in/BR/nickld.png",
            "background": f"{server}https://lo1.in/BR/nickld.png",
            "description": "Canal BR| NICKELODEON HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171344.m3u8",
                    "title": "BR| NICKELODEON HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal170",
            "type": "tv",
            "name": "✦●✦ MUSIC✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ MUSIC✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355447.m3u8",
                    "title": "✦●✦ MUSIC✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal171",
            "type": "tv",
            "name": "BR| VH1 HD",
            "poster": f"{server}https://lo1.in/BR/vh1.png",
            "background": f"{server}https://lo1.in/BR/vh1.png",
            "description": "Canal BR| VH1 HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162557.m3u8",
                    "title": "BR| VH1 HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal172",
            "type": "tv",
            "name": "✦●✦ NEWS ✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ NEWS ✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/355443.m3u8",
                    "title": "✦●✦ NEWS ✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal173",
            "type": "tv",
            "name": "BR| CNN BRASIL HD",
            "poster": f"{server}https://lo1.in/BR/cnnbrs.png",
            "background": f"{server}https://lo1.in/BR/cnnbrs.png",
            "description": "Canal BR| CNN BRASIL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162326.m3u8",
                    "title": "BR| CNN BRASIL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal174",
            "type": "tv",
            "name": "BR| CNN INTERNACIONAL HD",
            "poster": f"{server}https://lo1.in/BR/cnnint.png",
            "background": f"{server}https://lo1.in/BR/cnnint.png",
            "description": "Canal BR| CNN INTERNACIONAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/360177.m3u8",
                    "title": "BR| CNN INTERNACIONAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal175",
            "type": "tv",
            "name": "BR| GLOBO BRASILIA HD",
            "poster": f"{server}https://lo1.in/BR/glbbr.png",
            "background": f"{server}https://lo1.in/BR/glbbr.png",
            "description": "Canal BR| GLOBO BRASILIA HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162393.m3u8",
                    "title": "BR| GLOBO BRASILIA HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal176",
            "type": "tv",
            "name": "BR| GLOBO EPTV CAMPINAS HD",
            "poster": f"{server}https://lo1.in/BR/glboca.png",
            "background": f"{server}https://lo1.in/BR/glboca.png",
            "description": "Canal BR| GLOBO EPTV CAMPINAS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162396.m3u8",
                    "title": "BR| GLOBO EPTV CAMPINAS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal177",
            "type": "tv",
            "name": "BR| GLOBO EPTV SAO CARLOS HD",
            "poster": f"{server}https://lo1.in/BR/glboca.png",
            "background": f"{server}https://lo1.in/BR/glboca.png",
            "description": "Canal BR| GLOBO EPTV SAO CARLOS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162399.m3u8",
                    "title": "BR| GLOBO EPTV SAO CARLOS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal178",
            "type": "tv",
            "name": "BR| GLOBO NSC FLORIANOPOLIS HD",
            "poster": f"{server}https://lo1.in/BR/glbo.png",
            "background": f"{server}https://lo1.in/BR/glbo.png",
            "description": "Canal BR| GLOBO NSC FLORIANOPOLIS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331225.m3u8",
                    "title": "BR| GLOBO NSC FLORIANOPOLIS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal179",
            "type": "tv",
            "name": "BR| GLOBO MINAS HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO MINAS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162405.m3u8",
                    "title": "BR| GLOBO MINAS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal180",
            "type": "tv",
            "name": "BR| GLOBO NEWS HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO NEWS HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162406.m3u8",
                    "title": "BR| GLOBO NEWS HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal181",
            "type": "tv",
            "name": "BR| GLOBO NORDESTE HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO NORDESTE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162407.m3u8",
                    "title": "BR| GLOBO NORDESTE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal182",
            "type": "tv",
            "name": "BR| GLOBO RBS PORTO ALEGRE HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO RBS PORTO ALEGRE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162409.m3u8",
                    "title": "BR| GLOBO RBS PORTO ALEGRE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal183",
            "type": "tv",
            "name": "BR| GLOBO RIO GRANDE DO NORTE HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO RIO GRANDE DO NORTE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162412.m3u8",
                    "title": "BR| GLOBO RIO GRANDE DO NORTE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal184",
            "type": "tv",
            "name": "BR| GLOBO RJ HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO RJ HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162413.m3u8",
                    "title": "BR| GLOBO RJ HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal185",
            "type": "tv",
            "name": "BR| GLOBO SP HD",
            "poster": f"{server}https://lo1.in/BR/glbo.png",
            "background": f"{server}https://lo1.in/BR/glbo.png",
            "description": "Canal BR| GLOBO SP HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331224.m3u8",
                    "title": "BR| GLOBO SP HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal186",
            "type": "tv",
            "name": "BR| GLOBO TV BELEM HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO TV BELEM HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162418.m3u8",
                    "title": "BR| GLOBO TV BELEM HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal187",
            "type": "tv",
            "name": "BR| GLOBO TV HD",
            "poster": f"{server}https://lo1.in/BR/glbo.png",
            "background": f"{server}https://lo1.in/BR/glbo.png",
            "description": "Canal BR| GLOBO TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331227.m3u8",
                    "title": "BR| GLOBO TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal188",
            "type": "tv",
            "name": "BR| GLOBO TV PORTUGAL HD",
            "poster": f"{server}https://lo1.in/BR/glbo.png",
            "background": f"{server}https://lo1.in/BR/glbo.png",
            "description": "Canal BR| GLOBO TV PORTUGAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331226.m3u8",
                    "title": "BR| GLOBO TV PORTUGAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal189",
            "type": "tv",
            "name": "BR| GLOBO TV SERGIPE HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO TV SERGIPE HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162420.m3u8",
                    "title": "BR| GLOBO TV SERGIPE HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal190",
            "type": "tv",
            "name": "BR| GLOBOSAT HD",
            "poster": f"{server}https://lo1.in/BR/glbst0.png",
            "background": f"{server}https://lo1.in/BR/glbst0.png",
            "description": "Canal BR| GLOBOSAT HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162427.m3u8",
                    "title": "BR| GLOBOSAT HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal191",
            "type": "tv",
            "name": "BR| GLOBO INTERNACIONAL HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO INTERNACIONAL HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162403.m3u8",
                    "title": "BR| GLOBO INTERNACIONAL HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal192",
            "type": "tv",
            "name": "BR| GLOBO RPC TV HD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO RPC TV HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162415.m3u8",
                    "title": "BR| GLOBO RPC TV HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal193",
            "type": "tv",
            "name": "BR| GLOBO BAURU HD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| GLOBO BAURU HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/37416.m3u8",
                    "title": "BR| GLOBO BAURU HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal194",
            "type": "tv",
            "name": "BR| GLOBO BAHIA",
            "poster": f"{server}https://lo1.in/BR/glbo.png",
            "background": f"{server}https://lo1.in/BR/glbo.png",
            "description": "Canal BR| GLOBO BAHIA ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/53102.m3u8",
                    "title": "BR| GLOBO BAHIA",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal195",
            "type": "tv",
            "name": "BR| GLOOB HD",
            "poster": f"{server}https://lo1.in/BR/glb.png",
            "background": f"{server}https://lo1.in/BR/glb.png",
            "description": "Canal BR| GLOOB HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162428.m3u8",
                    "title": "BR| GLOOB HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal196",
            "type": "tv",
            "name": "BR| TV RA TIM BUM HD",
            "poster": f"{server}https://lo1.in/BR/ratim.png",
            "background": f"{server}https://lo1.in/BR/ratim.png",
            "description": "Canal BR| TV RA TIM BUM HD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162549.m3u8",
                    "title": "BR| TV RA TIM BUM HD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal197",
            "type": "tv",
            "name": "✦●✦ BRAZIL FHD✦●✦",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal ✦●✦ BRAZIL FHD✦●✦ ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171282.m3u8",
                    "title": "✦●✦ BRAZIL FHD✦●✦",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal198",
            "type": "tv",
            "name": "BR| A&E FHD",
            "poster": f"{server}https://lo1.in/BR/ane.png",
            "background": f"{server}https://lo1.in/BR/ane.png",
            "description": "Canal BR| A&E FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162298.m3u8",
                    "title": "BR| A&E FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal199",
            "type": "tv",
            "name": "BR| ARTE 1 FHD",
            "poster": f"{server}https://lo1.in/BR/art.png",
            "background": f"{server}https://lo1.in/BR/art.png",
            "description": "Canal BR| ARTE 1 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162306.m3u8",
                    "title": "BR| ARTE 1 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal200",
            "type": "tv",
            "name": "BR| AXN FHD",
            "poster": f"{server}https://lo1.in/BR/axn.png",
            "background": f"{server}https://lo1.in/BR/axn.png",
            "description": "Canal BR| AXN FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162307.m3u8",
                    "title": "BR| AXN FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal201",
            "type": "tv",
            "name": "BR| BIS FHD",
            "poster": f"{server}https://lo1.in/BR/bis.png",
            "background": f"{server}https://lo1.in/BR/bis.png",
            "description": "Canal BR| BIS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162314.m3u8",
                    "title": "BR| BIS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal202",
            "type": "tv",
            "name": "BR| CANAL BRASIL FHD",
            "poster": f"{server}https://lo1.in/BR/cnlbrs.png",
            "background": f"{server}https://lo1.in/BR/cnlbrs.png",
            "description": "Canal BR| CANAL BRASIL FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171267.m3u8",
                    "title": "BR| CANAL BRASIL FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal203",
            "type": "tv",
            "name": "BR| CANAL SONY FHD",
            "poster": f"{server}https://lo1.in/BR/sny.png",
            "background": f"{server}https://lo1.in/BR/sny.png",
            "description": "Canal BR| CANAL SONY FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162318.m3u8",
                    "title": "BR| CANAL SONY FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal204",
            "type": "tv",
            "name": "BR| CARTOONITO FHD",
            "poster": f"{server}https://lo1.in/BR/crtnet.png",
            "background": f"{server}https://lo1.in/BR/crtnet.png",
            "description": "Canal BR| CARTOONITO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162322.m3u8",
                    "title": "BR| CARTOONITO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal205",
            "type": "tv",
            "name": "BR| CINEMAX FHD",
            "poster": f"{server}https://lo1.in/BR/cinmx.png",
            "background": f"{server}https://lo1.in/BR/cinmx.png",
            "description": "Canal BR| CINEMAX FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162325.m3u8",
                    "title": "BR| CINEMAX FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal206",
            "type": "tv",
            "name": "BR| COMBATE FHD",
            "poster": f"{server}https://lo1.in/BR/combt.png",
            "background": f"{server}https://lo1.in/BR/combt.png",
            "description": "Canal BR| COMBATE FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162328.m3u8",
                    "title": "BR| COMBATE FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal207",
            "type": "tv",
            "name": "BR| COMEDY CENTRAL FHD",
            "poster": f"{server}https://lo1.in/BR/cmdcnt.png",
            "background": f"{server}https://lo1.in/BR/cmdcnt.png",
            "description": "Canal BR| COMEDY CENTRAL FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162330.m3u8",
                    "title": "BR| COMEDY CENTRAL FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal208",
            "type": "tv",
            "name": "BR| DISCOVERY CHANNEL FHD",
            "poster": f"{server}https://lo1.in/BR/disch.png",
            "background": f"{server}https://lo1.in/BR/disch.png",
            "description": "Canal BR| DISCOVERY CHANNEL FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162339.m3u8",
                    "title": "BR| DISCOVERY CHANNEL FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal209",
            "type": "tv",
            "name": "BR| DISCOVERY  H&amp;H FHD",
            "poster": f"{server}https://lo1.in/BR/dish.png",
            "background": f"{server}https://lo1.in/BR/dish.png",
            "description": "Canal BR| DISCOVERY  H&amp;H FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162342.m3u8",
                    "title": "BR| DISCOVERY  H&amp;H FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal210",
            "type": "tv",
            "name": "BR| DISCOVERY KIDS FHD",
            "poster": f"{server}https://lo1.in/BR/diskds.png",
            "background": f"{server}https://lo1.in/BR/diskds.png",
            "description": "Canal BR| DISCOVERY KIDS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162343.m3u8",
                    "title": "BR| DISCOVERY KIDS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal211",
            "type": "tv",
            "name": "BR| DISCOVERY THEATER FHD",
            "poster": f"{server}https://lo1.in/BR/disthe.png",
            "background": f"{server}https://lo1.in/BR/disthe.png",
            "description": "Canal BR| DISCOVERY THEATER FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162345.m3u8",
                    "title": "BR| DISCOVERY THEATER FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal212",
            "type": "tv",
            "name": "BR| DISCOVERY TLC FHD",
            "poster": f"{server}https://lo1.in/BR/distlc.png",
            "background": f"{server}https://lo1.in/BR/distlc.png",
            "description": "Canal BR| DISCOVERY TLC FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162518.m3u8",
                    "title": "BR| DISCOVERY TLC FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal213",
            "type": "tv",
            "name": "BR| DISCOVERY TURBO FHD",
            "poster": f"{server}https://lo1.in/BR/distrb.png",
            "background": f"{server}https://lo1.in/BR/distrb.png",
            "description": "Canal BR| DISCOVERY TURBO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162347.m3u8",
                    "title": "BR| DISCOVERY TURBO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal214",
            "type": "tv",
            "name": "BR| DISCOVERY WORLD FHD",
            "poster": f"{server}https://lo1.in/BR/diswrd.png",
            "background": f"{server}https://lo1.in/BR/diswrd.png",
            "description": "Canal BR| DISCOVERY WORLD FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162348.m3u8",
                    "title": "BR| DISCOVERY WORLD FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal215",
            "type": "tv",
            "name": "BR| DISNEY CHANNEL FHD",
            "poster": f"{server}https://lo1.in/BR/dsych.png",
            "background": f"{server}https://lo1.in/BR/dsych.png",
            "description": "Canal BR| DISNEY CHANNEL FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162349.m3u8",
                    "title": "BR| DISNEY CHANNEL FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal216",
            "type": "tv",
            "name": "BR| DISNEY JR FHD",
            "poster": f"{server}https://lo1.in/BR/nkjnr.png",
            "background": f"{server}https://lo1.in/BR/nkjnr.png",
            "description": "Canal BR| DISNEY JR FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162350.m3u8",
                    "title": "BR| DISNEY JR FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal217",
            "type": "tv",
            "name": "BR| FISH TV FHD",
            "poster": f"{server}https://lo1.in/BR/fish.png",
            "background": f"{server}https://lo1.in/BR/fish.png",
            "description": "Canal BR| FISH TV FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162370.m3u8",
                    "title": "BR| FISH TV FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal218",
            "type": "tv",
            "name": "BR| FONTE TV FHD",
            "poster": f"{server}https://lo1.in/BR/font.png",
            "background": f"{server}https://lo1.in/BR/font.png",
            "description": "Canal BR| FONTE TV FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162372.m3u8",
                    "title": "BR| FONTE TV FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal219",
            "type": "tv",
            "name": "BR| FOX FHD",
            "poster": f"{server}https://lo1.in/BR/fox.png",
            "background": f"{server}https://lo1.in/BR/fox.png",
            "description": "Canal BR| FOX FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162375.m3u8",
                    "title": "BR| FOX FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal220",
            "type": "tv",
            "name": "BR| FOX SPORTS 2 FHD",
            "poster": f"{server}https://lo1.in/BR/fxsp.png",
            "background": f"{server}https://lo1.in/BR/fxsp.png",
            "description": "Canal BR| FOX SPORTS 2 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162379.m3u8",
                    "title": "BR| FOX SPORTS 2 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal221",
            "type": "tv",
            "name": "BR| FOX SPORTS FHD",
            "poster": f"{server}https://lo1.in/BR/fxsp.png",
            "background": f"{server}https://lo1.in/BR/fxsp.png",
            "description": "Canal BR| FOX SPORTS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162382.m3u8",
                    "title": "BR| FOX SPORTS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal222",
            "type": "tv",
            "name": "BR| FX FHD",
            "poster": f"{server}https://lo1.in/BR/fx.png",
            "background": f"{server}https://lo1.in/BR/fx.png",
            "description": "Canal BR| FX FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162387.m3u8",
                    "title": "BR| FX FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal223",
            "type": "tv",
            "name": "BR| GLOOB FHD",
            "poster": f"{server}https://lo1.in/BR/glb.png",
            "background": f"{server}https://lo1.in/BR/glb.png",
            "description": "Canal BR| GLOOB FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171260.m3u8",
                    "title": "BR| GLOOB FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal224",
            "type": "tv",
            "name": "BR| GLOBO NEWS FHD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO NEWS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171279.m3u8",
                    "title": "BR| GLOBO NEWS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal225",
            "type": "tv",
            "name": "BR| GLOBO SP FHD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO SP FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162416.m3u8",
                    "title": "BR| GLOBO SP FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal226",
            "type": "tv",
            "name": "BR| GNT FHD",
            "poster": f"{server}https://lo1.in/BR/gnt.png",
            "background": f"{server}https://lo1.in/BR/gnt.png",
            "description": "Canal BR| GNT FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162430.m3u8",
                    "title": "BR| GNT FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal227",
            "type": "tv",
            "name": "BR| JOVEM PAN News FHD",
            "poster": f"{server}https://lo1.in/BR/flag.png",
            "background": f"{server}https://lo1.in/BR/flag.png",
            "description": "Canal BR| JOVEM PAN News FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/42802.m3u8",
                    "title": "BR| JOVEM PAN News FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal228",
            "type": "tv",
            "name": "BR| HBO 2 FHD",
            "poster": f"{server}https://lo1.in/BR/hbo2.png",
            "background": f"{server}https://lo1.in/BR/hbo2.png",
            "description": "Canal BR| HBO 2 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162433.m3u8",
                    "title": "BR| HBO 2 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal229",
            "type": "tv",
            "name": "BR| HBO FAMILY FHD",
            "poster": f"{server}https://lo1.in/BR/hbofm.png",
            "background": f"{server}https://lo1.in/BR/hbofm.png",
            "description": "Canal BR| HBO FAMILY FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162435.m3u8",
                    "title": "BR| HBO FAMILY FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal230",
            "type": "tv",
            "name": "BR| HBO FHD",
            "poster": f"{server}https://lo1.in/BR/hbo.png",
            "background": f"{server}https://lo1.in/BR/hbo.png",
            "description": "Canal BR| HBO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162436.m3u8",
                    "title": "BR| HBO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal231",
            "type": "tv",
            "name": "BR| HBO PLUS FHD",
            "poster": f"{server}https://lo1.in/BR/hbopl.png",
            "background": f"{server}https://lo1.in/BR/hbopl.png",
            "description": "Canal BR| HBO PLUS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162437.m3u8",
                    "title": "BR| HBO PLUS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal232",
            "type": "tv",
            "name": "BR| HBO SIGNATURE FHD",
            "poster": f"{server}https://lo1.in/BR/hbosignat.png",
            "background": f"{server}https://lo1.in/BR/hbosignat.png",
            "description": "Canal BR| HBO SIGNATURE FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162438.m3u8",
                    "title": "BR| HBO SIGNATURE FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal233",
            "type": "tv",
            "name": "BR| LIFE TIME FHD",
            "poster": f"{server}https://lo1.in/BR/lftm.png",
            "background": f"{server}https://lo1.in/BR/lftm.png",
            "description": "Canal BR| LIFE TIME FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162445.m3u8",
                    "title": "BR| LIFE TIME FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal234",
            "type": "tv",
            "name": "BR| HBO MUNDI FHD",
            "poster": f"{server}https://lo1.in/BR/hbom.png",
            "background": f"{server}https://lo1.in/BR/hbom.png",
            "description": "Canal BR| HBO MUNDI FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162448.m3u8",
                    "title": "BR| HBO MUNDI FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal235",
            "type": "tv",
            "name": "BR| HBO XTREME FHD",
            "poster": f"{server}https://lo1.in/BR/hboxtr.png",
            "background": f"{server}https://lo1.in/BR/hboxtr.png",
            "description": "Canal BR| HBO XTREME FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162449.m3u8",
                    "title": "BR| HBO XTREME FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal236",
            "type": "tv",
            "name": "BR| HBO POP FHD",
            "poster": f"{server}https://lo1.in/BR/hbopo.png",
            "background": f"{server}https://lo1.in/BR/hbopo.png",
            "description": "Canal BR| HBO POP FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162453.m3u8",
                    "title": "BR| HBO POP FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal237",
            "type": "tv",
            "name": "BR| MEGA PIX FHD",
            "poster": f"{server}https://lo1.in/BR/megapx.png",
            "background": f"{server}https://lo1.in/BR/megapx.png",
            "description": "Canal BR| MEGA PIX FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162454.m3u8",
                    "title": "BR| MEGA PIX FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal238",
            "type": "tv",
            "name": "BR| MTV BRAZIL FHD",
            "poster": f"{server}https://lo1.in/BR/mtvbr.png",
            "background": f"{server}https://lo1.in/BR/mtvbr.png",
            "description": "Canal BR| MTV BRAZIL FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162455.m3u8",
                    "title": "BR| MTV BRAZIL FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal239",
            "type": "tv",
            "name": "BR| NAT GEO FHD",
            "poster": f"{server}https://lo1.in/BR/natgeo.png",
            "background": f"{server}https://lo1.in/BR/natgeo.png",
            "description": "Canal BR| NAT GEO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162458.m3u8",
                    "title": "BR| NAT GEO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal240",
            "type": "tv",
            "name": "BR| NAT GEO KIDS FHD",
            "poster": f"{server}https://lo1.in/BR/natgeok.png",
            "background": f"{server}https://lo1.in/BR/natgeok.png",
            "description": "Canal BR| NAT GEO KIDS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162459.m3u8",
                    "title": "BR| NAT GEO KIDS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal241",
            "type": "tv",
            "name": "BR| NOVA ERA TV FHD",
            "poster": f"{server}https://lo1.in/BR/novaer.png",
            "background": f"{server}https://lo1.in/BR/novaer.png",
            "description": "Canal BR| NOVA ERA TV FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397468.m3u8",
                    "title": "BR| NOVA ERA TV FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal242",
            "type": "tv",
            "name": "BR| PREMIER FHD",
            "poster": f"{server}https://lo1.in/BR/prm.png",
            "background": f"{server}https://lo1.in/BR/prm.png",
            "description": "Canal BR| PREMIER FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162467.m3u8",
                    "title": "BR| PREMIER FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal243",
            "type": "tv",
            "name": "BR| RECORD SP FHD",
            "poster": f"{server}https://lo1.in/BR/rcord.png",
            "background": f"{server}https://lo1.in/BR/rcord.png",
            "description": "Canal BR| RECORD SP FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162488.m3u8",
                    "title": "BR| RECORD SP FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal244",
            "type": "tv",
            "name": "BR| SBT FHD",
            "poster": f"{server}https://lo1.in/BR/sbt.png",
            "background": f"{server}https://lo1.in/BR/sbt.png",
            "description": "Canal BR| SBT FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/171292.m3u8",
                    "title": "BR| SBT FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal245",
            "type": "tv",
            "name": "BR| SPORTV 2 FHD",
            "poster": f"{server}https://lo1.in/BR/spt2.png",
            "background": f"{server}https://lo1.in/BR/spt2.png",
            "description": "Canal BR| SPORTV 2 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162502.m3u8",
                    "title": "BR| SPORTV 2 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal246",
            "type": "tv",
            "name": "BR| SPORTV 3 FHD",
            "poster": f"{server}https://lo1.in/BR/spt3.png",
            "background": f"{server}https://lo1.in/BR/spt3.png",
            "description": "Canal BR| SPORTV 3 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162503.m3u8",
                    "title": "BR| SPORTV 3 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal247",
            "type": "tv",
            "name": "BR| SPORTV FHD",
            "poster": f"{server}https://lo1.in/BR/sp.png",
            "background": f"{server}https://lo1.in/BR/sp.png",
            "description": "Canal BR| SPORTV FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162504.m3u8",
                    "title": "BR| SPORTV FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal248",
            "type": "tv",
            "name": "BR| TELECINE ACTION FHD",
            "poster": f"{server}https://lo1.in/BR/telact.png",
            "background": f"{server}https://lo1.in/BR/telact.png",
            "description": "Canal BR| TELECINE ACTION FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162510.m3u8",
                    "title": "BR| TELECINE ACTION FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal249",
            "type": "tv",
            "name": "BR| TELECINE FUN FHD",
            "poster": f"{server}https://lo1.in/BR/telcef.png",
            "background": f"{server}https://lo1.in/BR/telcef.png",
            "description": "Canal BR| TELECINE FUN FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162512.m3u8",
                    "title": "BR| TELECINE FUN FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal250",
            "type": "tv",
            "name": "BR| TELECINE PIPOCA FHD",
            "poster": f"{server}https://lo1.in/BR/telpipo.png",
            "background": f"{server}https://lo1.in/BR/telpipo.png",
            "description": "Canal BR| TELECINE PIPOCA FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162513.m3u8",
                    "title": "BR| TELECINE PIPOCA FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal251",
            "type": "tv",
            "name": "BR| TELECINE PREMIUM FHD",
            "poster": f"{server}https://lo1.in/BR/telcnpr.png",
            "background": f"{server}https://lo1.in/BR/telcnpr.png",
            "description": "Canal BR| TELECINE PREMIUM FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162514.m3u8",
                    "title": "BR| TELECINE PREMIUM FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal252",
            "type": "tv",
            "name": "BR| TELECINE TOUCH FHD",
            "poster": f"{server}https://lo1.in/BR/telcnto.png",
            "background": f"{server}https://lo1.in/BR/telcnto.png",
            "description": "Canal BR| TELECINE TOUCH FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162515.m3u8",
                    "title": "BR| TELECINE TOUCH FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal253",
            "type": "tv",
            "name": "BR| TNT FHD",
            "poster": f"{server}https://lo1.in/BR/tnt.png",
            "background": f"{server}https://lo1.in/BR/tnt.png",
            "description": "Canal BR| TNT FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162519.m3u8",
                    "title": "BR| TNT FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal254",
            "type": "tv",
            "name": "BR| TNT SERIES FHD",
            "poster": f"{server}https://lo1.in/BR/tntser.png",
            "background": f"{server}https://lo1.in/BR/tntser.png",
            "description": "Canal BR| TNT SERIES FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162520.m3u8",
                    "title": "BR| TNT SERIES FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal255",
            "type": "tv",
            "name": "BR| TOONCAST FHD",
            "poster": f"{server}https://lo1.in/BR/tonc.png",
            "background": f"{server}https://lo1.in/BR/tonc.png",
            "description": "Canal BR| TOONCAST FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162521.m3u8",
                    "title": "BR| TOONCAST FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal256",
            "type": "tv",
            "name": "BR| TV APARECIDA FHD",
            "poster": f"{server}https://lo1.in/BR/apra.png",
            "background": f"{server}https://lo1.in/BR/apra.png",
            "description": "Canal BR| TV APARECIDA FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/331233.m3u8",
                    "title": "BR| TV APARECIDA FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal257",
            "type": "tv",
            "name": "BR| TV EDUCATIVA DE PORTO ALEGRE FHD",
            "poster": f"{server}https://lo1.in/BR/edutoa.png",
            "background": f"{server}https://lo1.in/BR/edutoa.png",
            "description": "Canal BR| TV EDUCATIVA DE PORTO ALEGRE FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/397466.m3u8",
                    "title": "BR| TV EDUCATIVA DE PORTO ALEGRE FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal258",
            "type": "tv",
            "name": "BR| TV GAZETA FHD",
            "poster": f"{server}https://lo1.in/BR/tgaze.png",
            "background": f"{server}https://lo1.in/BR/tgaze.png",
            "description": "Canal BR| TV GAZETA FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162538.m3u8",
                    "title": "BR| TV GAZETA FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal259",
            "type": "tv",
            "name": "BR| TV NOVO TEMPO FHD",
            "poster": f"{server}https://lo1.in/BR/novotem.png",
            "background": f"{server}https://lo1.in/BR/novotem.png",
            "description": "Canal BR| TV NOVO TEMPO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380045.m3u8",
                    "title": "BR| TV NOVO TEMPO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal260",
            "type": "tv",
            "name": "BR| UNIVERSAL TV FHD",
            "poster": f"{server}https://lo1.in/BR/univ.png",
            "background": f"{server}https://lo1.in/BR/univ.png",
            "description": "Canal BR| UNIVERSAL TV FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/380041.m3u8",
                    "title": "BR| UNIVERSAL TV FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal261",
            "type": "tv",
            "name": "BR| VIVA FHD",
            "poster": f"{server}https://lo1.in/BR/viva.png",
            "background": f"{server}https://lo1.in/BR/viva.png",
            "description": "Canal BR| VIVA FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162560.m3u8",
                    "title": "BR| VIVA FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal262",
            "type": "tv",
            "name": "BR| WARNER BROS FHD",
            "poster": f"{server}https://lo1.in/BR/warnch.png",
            "background": f"{server}https://lo1.in/BR/warnch.png",
            "description": "Canal BR| WARNER BROS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162561.m3u8",
                    "title": "BR| WARNER BROS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal263",
            "type": "tv",
            "name": "BR| WOHOO FHD",
            "poster": f"{server}https://lo1.in/BR/woho.png",
            "background": f"{server}https://lo1.in/BR/woho.png",
            "description": "Canal BR| WOHOO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162562.m3u8",
                    "title": "BR| WOHOO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal264",
            "type": "tv",
            "name": "BR| ZOOMOO FHD",
            "poster": f"{server}https://lo1.in/BR/zomo.png",
            "background": f"{server}https://lo1.in/BR/zomo.png",
            "description": "Canal BR| ZOOMOO FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162564.m3u8",
                    "title": "BR| ZOOMOO FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal265",
            "type": "tv",
            "name": "BR| GLOBO RBS PORTO ALEGRE FHD",
            "poster": f"{server}https://lo1.in/BR/globi.png",
            "background": f"{server}https://lo1.in/BR/globi.png",
            "description": "Canal BR| GLOBO RBS PORTO ALEGRE FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162410.m3u8",
                    "title": "BR| GLOBO RBS PORTO ALEGRE FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal266",
            "type": "tv",
            "name": "BR| RECORD AMAZONAS FHD",
            "poster": f"{server}https://lo1.in/BR/rcodamz.png",
            "background": f"{server}https://lo1.in/BR/rcodamz.png",
            "description": "Canal BR| RECORD AMAZONAS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162478.m3u8",
                    "title": "BR| RECORD AMAZONAS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal267",
            "type": "tv",
            "name": "BR| BAND CAMPINAS FHD",
            "poster": f"{server}https://lo1.in/BR/band.png",
            "background": f"{server}https://lo1.in/BR/band.png",
            "description": "Canal BR| BAND CAMPINAS FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162310.m3u8",
                    "title": "BR| BAND CAMPINAS FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal268",
            "type": "tv",
            "name": "BR| TELECINE CULT FHD",
            "poster": f"{server}https://lo1.in/BR/telcu.png",
            "background": f"{server}https://lo1.in/BR/telcu.png",
            "description": "Canal BR| TELECINE CULT FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162511.m3u8",
                    "title": "BR| TELECINE CULT FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal269",
            "type": "tv",
            "name": "BR| TRAVEL BOX FHD",
            "poster": f"{server}https://lo1.in/BR/trvbx.png",
            "background": f"{server}https://lo1.in/BR/trvbx.png",
            "description": "Canal BR| TRAVEL BOX FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/162522.m3u8",
                    "title": "BR| TRAVEL BOX FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal270",
            "type": "tv",
            "name": "BR| PARAMOUNT+ 01 FHD",
            "poster": f"{server}https://lo1.in/BR/paramch.png",
            "background": f"{server}https://lo1.in/BR/paramch.png",
            "description": "Canal BR| PARAMOUNT+ 01 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/52283.m3u8",
                    "title": "BR| PARAMOUNT+ 01 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal271",
            "type": "tv",
            "name": "BR| PARAMOUNT+ 02 FHD",
            "poster": f"{server}https://lo1.in/BR/paramch.png",
            "background": f"{server}https://lo1.in/BR/paramch.png",
            "description": "Canal BR| PARAMOUNT+ 02 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/52282.m3u8",
                    "title": "BR| PARAMOUNT+ 02 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal272",
            "type": "tv",
            "name": "BR| PARAMOUNT+ 03 FHD",
            "poster": f"{server}https://lo1.in/BR/paramch.png",
            "background": f"{server}https://lo1.in/BR/paramch.png",
            "description": "Canal BR| PARAMOUNT+ 03 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/52281.m3u8",
                    "title": "BR| PARAMOUNT+ 03 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
        {
            "id": "iptv:canal273",
            "type": "tv",
            "name": "BR| PARAMOUNT+ 04 FHD",
            "poster": f"{server}https://lo1.in/BR/paramch.png",
            "background": f"{server}https://lo1.in/BR/paramch.png",
            "description": "Canal BR| PARAMOUNT+ 04 FHD ao vivo.",
            "genres": ["IPTV"],
            "streams": [
                {
                    "url": "http://zkbvzkj.megahdtv.xyz:80/live/1103581436/4099381829/52280.m3u8",
                    "title": "BR| PARAMOUNT+ 04 FHD",
                    "behaviorHints": {
                        "notWebReady": True
                    }
                }
            ]
        },
    ]
    return canais
