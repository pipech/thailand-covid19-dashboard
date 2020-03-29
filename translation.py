def _(text, lang='TH'):
    th_dict = {
        # country name
        'Thailand': 'ประเทศไทย',
        'US': 'สหรัฐอเมริกา',
        'Spain': 'สเปน',
        'Italy': 'อิตาลี',
        'China': 'จีน',
        'Iran': 'อิหร่าน',
        'United Kingdom': 'สหราชอาณาจักร',
        'Japan': 'ญี่ปุ่น',
        'Singapore': 'สิงคโปร์',
        'Hong Kong': 'ฮ่องกง',
        # text
        'Double case <br> every {} day(s)':
            'ผู้ติดเชื้อเพิ่มขึ้นเป็นสองเท่า<br>ทุก {} วัน',
        'Cumulative number of confirmed cases':
            'จำนวนติดเชื้อสะสม',
        'Number of days since 100th case':
            'จำนวนวันหลังพบผู้ติดเชื้อครบ 100 คน',
        'Thailand focus covid-19 dashboard':
            'สถานการณ์ผู้ติดเชื้อโควิด-19 ในประเทศไทย',
        'Cumulative number of confirm cases, by number of days since 100th case':
            'กราฟแสดงจำนวนผู้ติดเชื้อโควิด-19 สะสม นับจากวันที่มีผู้ติดเชื้อถึง 100 ราย',
        'Data source: ': 'แหล่งข้อมูล: ',
        'Graph reference: ': 'รูปแบบกราฟอ้างอิงจาก: ',
        'Data updated: {}': 'อัพเดทล่าสุด: {}',
        (
            'Days since 100th case: <b>%{x}</b><br>'
            'Confirm case: <b>%{y:,f}</b><br>'
            'Date: <b>%{text}</b>'
        ):
            (
                'จำนวนวันหลังพบผู้ติดเชื้อครบ 100 คน: <b>%{x}</b><br>'
                'จำนวนผู้ติดเชื้อ: <b>%{y:,f}</b><br>'
                'วันที่: <b>%{text}</b>'
            ),
        # meta
        'Covid19 tracking dashboard for Thailand, Daily updated':
            'อัพเดทข้อมูลรายวัน สถานการณ์ผู้ติดเชื้อโควิด-19 ในประเทศไทย',
    }

    translated_text = th_dict.get(text, text)

    return translated_text
