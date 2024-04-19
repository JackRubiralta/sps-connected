import requests
import datetime

cookies = {
    'S': 'spreadsheet_forms=-rozX44qaUe_0aTvz_vIh7nnhQHhajYV5YPLNbcqzZs',
    'COMPASS': 'spreadsheet_forms=CjIACWuJV1_Qb-7_yMdC9181-iCVhSu_A80keuSi5eRu7dK0k9ir6dLvAOg0blUbYGmfmRCYqLiuBhpUAAlriVdl2_yTe9HJxd8fo8Wlj1YCyEeBz43grtpTRvZunCCiEfQiBmxjbjiB3gEW50B3wps-USWXbvAr6U0PgIDEnETioDe9Kv71mn_dzGmg7_Py',
    '__Secure-ENID': '17.SE=DXs45ssMV3aR_u2wILXbX3Y0lp58fA-oD3hF_ryTwqxA6d99XOgbz9xPZz4IO4AXk13BrscSQZo4XWHsx-gN4xG5-3rPuurKVylkvX9cgaso2nJT85VvyvqPqssryhOk9ntRC07K3LmBHEiAp9JeV8nBbe7uxSAmsoqjNHKZu3w6I-m72TQFd7iOn82CymP9gAzZ3GDsahMinSQMnVEocPGGcm3TwcIA32F5vdryaOZGF-CxYHgBwTU2gMtVl9ExgM-borlQVXLg_XpwZwk7sbZJIE0vtzonEX4C-PY',
    'OTZ': '7415470_76_76_104100_72_446760',
    'SID': 'g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvgo8Z0WaA0B2Rx1RwI1kjoXAACgYKAYcSAQASFQHGX2MiN6F7gKzXMDu5mY71PDHvsBoVAUF8yKqLmuQeBlYsMiKOeGsH_TBE0076',
    '__Secure-1PSID': 'g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvgsjEG_JrcJfqE17sgiI3uvwACgYKAboSAQASFQHGX2Mi09VaBDk6avliZbSZ1IjHwxoVAUF8yKoSQ6pzn_5OC48Gsa8Aq2540076',
    '__Secure-3PSID': 'g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvg8ltnXmSmfa52NAlksQ3JEwACgYKAdkSAQASFQHGX2MiX7q--Wnpk6UBznezFlrfjhoVAUF8yKoJ1dSECafaclvFntzCXU-D0076',
    'HSID': 'ATPzXc9CStMxKIb4F',
    'SSID': 'AfLW3z2uCDBzKB6Lw',
    'APISID': 'dlSzodvsdxnHKLo9/AsMlpeUaOVfpZXYqZ',
    'SAPISID': 'yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll',
    '__Secure-1PAPISID': 'yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll',
    '__Secure-3PAPISID': 'yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll',
    'OSID': 'g.a000gQj-RUdanBkuv7jGRI9SyjGmeY2uWbXFCVuUiB0oDioqQJw60-ZvWWz8x15HJwmIlCTaZAACgYKAdcSAQASFQHGX2MiPFBv43lzoPMz1J2XZLjCzxoVAUF8yKpdnCNCWM9a2iCm42Y7OM7W0076',
    '__Secure-OSID': 'g.a000gQj-RUdanBkuv7jGRI9SyjGmeY2uWbXFCVuUiB0oDioqQJw66kCkQhmylPYtrGXZjeJt6QACgYKASkSAQASFQHGX2MirMLcSXKorBFd2dXX1-_JtRoVAUF8yKrVEh8QJwYYEwZzadUPJ31u0076',
    'NID': '511=vMHMpLcSIIn73dJHEDWKfnccpZAjgxTtQDetf_6XiUg7czlP7qhdzN54UZhzKgjP7q-tVK7ieeoS_aBD2vddyxiXyn0gu8jB7Y9GnZv-8-_0nzqE7RrVn2uVlbcTiA-M5L5jtjrqk3p8EKIzkuq5nlGdLz3JaAP3UYWmLrDQzmiGf4rr8q5Nj8S59cjd6zKI_gwMg__5M5lL8XCnaTjgb3iWU-SVDkOIdtpgEljHCqC3Vffh07eC-pl8VfQ881XFw6WhhaFwNL4xBGZZn8FJkb2OXHD9ZFLgfyiDzkKVxLGUUjlW43eJbquJ0-WGbpzV2A8NlNeW-e5yX5_jrt-85Nubg__W5olPQM2pvaoiTYbgWO5FT7sBQW_tEcRnzYOqjPn986LOIoXyzoGGPMl_dF7E5jrgJ1aU6BNOIpzlaCW7Y55BFbRYC0ClIuMq2K0VFt8tUZtROVjqlGQwV2Vmaf-Sd-MuIL_lf5PvK6V531eymHd4PA',
    'AEC': 'Ae3NU9OIfNc1VTswsD7Roewc_0ct9udlOIfKUyOxeBlfqZ6yZG-xsw7yNL8',
    'COMPASS': 'blobstore-http-onepick-kix=CgAQ-p-qrgYafQAJa4lX_JcacuD59DgDoUGa1x2FBu1YRNyOKqk75Bqg7h2eV7EGC2wnIzeNudBT1_FLrvrsZ0GYqAnH9pztVnRdGsM1gqMGu4m66UXhh1cyGfU9QXNYS3FDAMcEJ_3CDlNlCV8xBpBWrikllDZCGXPiRKdoUtrwnpKi3ftBMAE:blobstore-http-onepick-drawings=CgAQ4NylrQYaggEACWuJV9mShvluhIzPC14OVXwEGznjaRfRkRYYyz_onmJ_H5cGeQBQM4aoVoltexbR--5QIgxf8VBkUWk_S_vDCT2UJQ_60JSl1Y3MoyCMKp6aFj_EQ-o35lQoOwciBzBoSRw2w-u-yYqNgdiKYkoSFrev25VmkorX1SK1uUjXpYR3MAE:blobstore-http-doplar-presentations=CgAQkozQrQYahgEACWuJVwPXLwWatZsYVFft-BhCpbsV5xkSE5Ko1lFXao-Ij38o2xnL9zo1izpxrY7pRkJ15ZM5VBWv9KVJKnGecMYwwuv4D0a7FyzbWP3awlFZAFV_NhM6Q4s2YuyQrHaOZx5s6CgS29-nxgNkWZrxFlTpJgPBFzJ2L-osl-CbQ5QoLAQJBDAB:blobstore-http-onepick-presentations=CgAQ-9K1rgYahQEACWuJV3klZF5S3Ydol2N3CaQbmmRB5SiqvL31c5jORAPbehBwzGX0woNAencl1lhusXeRIARZLYybuu155kZYrQuJjE2Jm-zNfYIfHu1iHiAxAO5WjQG_zvITJWCIqSZVSH9Sn59CRleH-BXI0OwkW221ChHU86wmnpdjNS_TyV1gE3CxMAE',
    '1P_JAR': '2024-2-15-12',
    '__Secure-1PSIDTS': 'sidts-CjEBYfD7Z1yvvp9phKSbV-Fj60SUX3OlinSdi9PM4cfuiMDPOFGoCAE2bQVoDINNIaOYEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBYfD7Z1yvvp9phKSbV-Fj60SUX3OlinSdi9PM4cfuiMDPOFGoCAE2bQVoDINNIaOYEAA',
    'SIDCC': 'ABTWhQEZqpsrVEZm8k1HVN8NrjbremBNmyPC6GV6rVhFdpMkIH-ED3cUsC8ARQO9ngI-NT4Daw',
    '__Secure-1PSIDCC': 'ABTWhQF6QZz7nCuoOazo8FZDlXMv4zqOnxbCwmELmbzQTMj0kTyapoPfn5_7ZkfSvQEDG6WbIg',
    '__Secure-3PSIDCC': 'ABTWhQHZ_QZc6GKIWtphXjVfhX2C6GD_Bg4eEdxymAA95gQYP1zcLit_l5XEK4xn29O3kULaGRA',
}

headers = {
    'authority': 'docs.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'S=spreadsheet_forms=-rozX44qaUe_0aTvz_vIh7nnhQHhajYV5YPLNbcqzZs; COMPASS=spreadsheet_forms=CjIACWuJV1_Qb-7_yMdC9181-iCVhSu_A80keuSi5eRu7dK0k9ir6dLvAOg0blUbYGmfmRCYqLiuBhpUAAlriVdl2_yTe9HJxd8fo8Wlj1YCyEeBz43grtpTRvZunCCiEfQiBmxjbjiB3gEW50B3wps-USWXbvAr6U0PgIDEnETioDe9Kv71mn_dzGmg7_Py; __Secure-ENID=17.SE=DXs45ssMV3aR_u2wILXbX3Y0lp58fA-oD3hF_ryTwqxA6d99XOgbz9xPZz4IO4AXk13BrscSQZo4XWHsx-gN4xG5-3rPuurKVylkvX9cgaso2nJT85VvyvqPqssryhOk9ntRC07K3LmBHEiAp9JeV8nBbe7uxSAmsoqjNHKZu3w6I-m72TQFd7iOn82CymP9gAzZ3GDsahMinSQMnVEocPGGcm3TwcIA32F5vdryaOZGF-CxYHgBwTU2gMtVl9ExgM-borlQVXLg_XpwZwk7sbZJIE0vtzonEX4C-PY; OTZ=7415470_76_76_104100_72_446760; SID=g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvgo8Z0WaA0B2Rx1RwI1kjoXAACgYKAYcSAQASFQHGX2MiN6F7gKzXMDu5mY71PDHvsBoVAUF8yKqLmuQeBlYsMiKOeGsH_TBE0076; __Secure-1PSID=g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvgsjEG_JrcJfqE17sgiI3uvwACgYKAboSAQASFQHGX2Mi09VaBDk6avliZbSZ1IjHwxoVAUF8yKoSQ6pzn_5OC48Gsa8Aq2540076; __Secure-3PSID=g.a000gQj-RXZvoZguqYis1dB7Bvv_2X4sZpHBjURkbkcKlo1VKjvg8ltnXmSmfa52NAlksQ3JEwACgYKAdkSAQASFQHGX2MiX7q--Wnpk6UBznezFlrfjhoVAUF8yKoJ1dSECafaclvFntzCXU-D0076; HSID=ATPzXc9CStMxKIb4F; SSID=AfLW3z2uCDBzKB6Lw; APISID=dlSzodvsdxnHKLo9/AsMlpeUaOVfpZXYqZ; SAPISID=yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll; __Secure-1PAPISID=yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll; __Secure-3PAPISID=yJuZImL7HgKU8LdF/Aar7GIjglCitDLcll; OSID=g.a000gQj-RUdanBkuv7jGRI9SyjGmeY2uWbXFCVuUiB0oDioqQJw60-ZvWWz8x15HJwmIlCTaZAACgYKAdcSAQASFQHGX2MiPFBv43lzoPMz1J2XZLjCzxoVAUF8yKpdnCNCWM9a2iCm42Y7OM7W0076; __Secure-OSID=g.a000gQj-RUdanBkuv7jGRI9SyjGmeY2uWbXFCVuUiB0oDioqQJw66kCkQhmylPYtrGXZjeJt6QACgYKASkSAQASFQHGX2MirMLcSXKorBFd2dXX1-_JtRoVAUF8yKrVEh8QJwYYEwZzadUPJ31u0076; NID=511=vMHMpLcSIIn73dJHEDWKfnccpZAjgxTtQDetf_6XiUg7czlP7qhdzN54UZhzKgjP7q-tVK7ieeoS_aBD2vddyxiXyn0gu8jB7Y9GnZv-8-_0nzqE7RrVn2uVlbcTiA-M5L5jtjrqk3p8EKIzkuq5nlGdLz3JaAP3UYWmLrDQzmiGf4rr8q5Nj8S59cjd6zKI_gwMg__5M5lL8XCnaTjgb3iWU-SVDkOIdtpgEljHCqC3Vffh07eC-pl8VfQ881XFw6WhhaFwNL4xBGZZn8FJkb2OXHD9ZFLgfyiDzkKVxLGUUjlW43eJbquJ0-WGbpzV2A8NlNeW-e5yX5_jrt-85Nubg__W5olPQM2pvaoiTYbgWO5FT7sBQW_tEcRnzYOqjPn986LOIoXyzoGGPMl_dF7E5jrgJ1aU6BNOIpzlaCW7Y55BFbRYC0ClIuMq2K0VFt8tUZtROVjqlGQwV2Vmaf-Sd-MuIL_lf5PvK6V531eymHd4PA; AEC=Ae3NU9OIfNc1VTswsD7Roewc_0ct9udlOIfKUyOxeBlfqZ6yZG-xsw7yNL8; COMPASS=blobstore-http-onepick-kix=CgAQ-p-qrgYafQAJa4lX_JcacuD59DgDoUGa1x2FBu1YRNyOKqk75Bqg7h2eV7EGC2wnIzeNudBT1_FLrvrsZ0GYqAnH9pztVnRdGsM1gqMGu4m66UXhh1cyGfU9QXNYS3FDAMcEJ_3CDlNlCV8xBpBWrikllDZCGXPiRKdoUtrwnpKi3ftBMAE:blobstore-http-onepick-drawings=CgAQ4NylrQYaggEACWuJV9mShvluhIzPC14OVXwEGznjaRfRkRYYyz_onmJ_H5cGeQBQM4aoVoltexbR--5QIgxf8VBkUWk_S_vDCT2UJQ_60JSl1Y3MoyCMKp6aFj_EQ-o35lQoOwciBzBoSRw2w-u-yYqNgdiKYkoSFrev25VmkorX1SK1uUjXpYR3MAE:blobstore-http-doplar-presentations=CgAQkozQrQYahgEACWuJVwPXLwWatZsYVFft-BhCpbsV5xkSE5Ko1lFXao-Ij38o2xnL9zo1izpxrY7pRkJ15ZM5VBWv9KVJKnGecMYwwuv4D0a7FyzbWP3awlFZAFV_NhM6Q4s2YuyQrHaOZx5s6CgS29-nxgNkWZrxFlTpJgPBFzJ2L-osl-CbQ5QoLAQJBDAB:blobstore-http-onepick-presentations=CgAQ-9K1rgYahQEACWuJV3klZF5S3Ydol2N3CaQbmmRB5SiqvL31c5jORAPbehBwzGX0woNAencl1lhusXeRIARZLYybuu155kZYrQuJjE2Jm-zNfYIfHu1iHiAxAO5WjQG_zvITJWCIqSZVSH9Sn59CRleH-BXI0OwkW221ChHU86wmnpdjNS_TyV1gE3CxMAE; 1P_JAR=2024-2-15-12; __Secure-1PSIDTS=sidts-CjEBYfD7Z1yvvp9phKSbV-Fj60SUX3OlinSdi9PM4cfuiMDPOFGoCAE2bQVoDINNIaOYEAA; __Secure-3PSIDTS=sidts-CjEBYfD7Z1yvvp9phKSbV-Fj60SUX3OlinSdi9PM4cfuiMDPOFGoCAE2bQVoDINNIaOYEAA; SIDCC=ABTWhQEZqpsrVEZm8k1HVN8NrjbremBNmyPC6GV6rVhFdpMkIH-ED3cUsC8ARQO9ngI-NT4Daw; __Secure-1PSIDCC=ABTWhQF6QZz7nCuoOazo8FZDlXMv4zqOnxbCwmELmbzQTMj0kTyapoPfn5_7ZkfSvQEDG6WbIg; __Secure-3PSIDCC=ABTWhQHZ_QZc6GKIWtphXjVfhX2C6GD_Bg4eEdxymAA95gQYP1zcLit_l5XEK4xn29O3kULaGRA',
    'dnt': '1',
    'origin': 'https://docs.google.com',
    'referer': 'https://docs.google.com/forms/d/e/1FAIpQLScPMOikOkEyQALyx79ltAz0AYlltd_kdNSy9qCPbu3FD6xQ3g/viewform?fbzx=8790350333793995156',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"121.0.6167.184"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.184", "Chromium";v="121.0.6167.184"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-client-data': 'CJW2yQEIprbJAQipncoBCJfnygEIk6HLAQiFoM0BCLjIzQEIoe7NAQjK7s0BCN3uzQEIg/DNAQia8s0BCOr3zQEIgvrNAQjf+s0BCPX6zQEI6/zNARiPzs0BGKfqzQEYmfjNARjJ+M0BGOuNpRc=',
}


# Get today's date
today = datetime.date.today()

# Calculate how many days to add to get to the next Tuesday (weekday() returns 0 for Monday, so 1 is Tuesday)
days_until_next_tuesday = (1 - today.weekday() + 7) % 7
if days_until_next_tuesday == 0:
    days_until_next_tuesday = 7  # If today is Tuesday, get the next Tuesday

# Calculate the date of the next Tuesday
next_tuesday = today + datetime.timedelta(days=days_until_next_tuesday)

# Format and print the date of the next Tuesday
next_tuesday_string = next_tuesday.strftime("%B %d")

data = {
    'entry.1980872933': f"Join the Computer Science Club Tonight, Tuesday, {next_tuesday_string}, from 7:00 p.m. to 8:00 p.m. in Friedman Project Room 111. We will be working on different coding problems and on our lost and found website. Everyone is welcome, regardless of skill level but don't forget to bring your laptop. For more information, contact jack.rubiraltakunze@sps.edu or henry.abrahamsen@sps.edu.",
    'entry.244056213': f'Tuesday, {next_tuesday_string} from 7:00 p.m. to 8:00 pm in Friedman Project Room 111',
    'entry.595880039': ' jack.rubiraltakunze@sps.edu or henry.abrahamsen@sps.edu',
    'entry.460653111': 'This was created using DALL E: https://drive.google.com/file/d/1-JWgr3qXqVqsIRWoIWZ3541eUqTeERN9/view?usp=sharing',
    'entry.1761044153': 'Nope',
    'entry.232551408': 'Event',
    'emailAddress': 'jack.rubiraltakunze@sps.edu',
    'dlut': '1708001201348',
    'entry.232551408_sentinel': '',
    'fvv': '1',
    'partialResponse': '[null,null,"8790350333793995156"]',
    'pageHistory': '0',
    'fbzx': '8790350333793995156',
}


response = requests.post(
    'https://docs.google.com/forms/u/0/d/e/1FAIpQLScPMOikOkEyQALyx79ltAz0AYlltd_kdNSy9qCPbu3FD6xQ3g/formResponse',
    cookies=cookies,
    headers=headers,
    data=data,
)

if response.status_code in [200, 302]:
    print(f"Success: {response.status_code}")
else:
    print(f"Error: {response.status_code}")

