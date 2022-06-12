def parse(query: str) -> dict:
    reformat = query.replace('/', '?').replace(':', '?').replace(';', '?').replace('&', '?').split('?')
    parsed_dict = {second[0]: second[1] for second in [first.split('=') for first in reformat if '=' in first]
                   if len(second[0]) > 1 and len(second[1]) > 1}
    return parsed_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page:name=ferret:color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=?') == {'name': 'ferret'}
    assert parse('http://example.com/?&name=Dima=') == {'name': 'Dima'}
    assert parse('http://example.com/?&=Dima/name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page:ferret/color:purple&name') == {}
    assert parse('https://example.com/path/to/?:color/=purple&&color=purple') == {'color': 'purple'}
    assert parse('http://example.com/?&=:;') == {}
    assert parse('http://example.com/?=Dima?=name/color=&=purple/') == {}
    assert parse('https://example.com/path/to/?:color/=purple==color/purlple') == {}
    assert parse('https://example.com/path/to/page?name=ferret=color=?') == {'name': 'ferret'}


def parse_cookie(query: str) -> dict:
    reformat = query.replace('/', '?').replace(':', '?').replace(';', '?').replace('&', '?').split('?')
    parsed_cookie = {
        second[0]: second[1] for second in [first.split('=', 1) for first in reformat if '=' in first]
        if (len(second[0]) > 1 and '=' not in second[:][0][0])
           and (len(second[1]) > 1 and '=' not in second[:][1][0])
    }
    return parsed_cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima//age==28;') == {'name': 'Dima'}
    assert parse_cookie('name==Dima//age==28;') == {}
    assert parse_cookie('name=/Dima;age=28;') == {'age': '28'}
    assert parse_cookie('name===Dima/User;age=28;') == {'age': '28'}
    assert parse_cookie('name/Dima:User;age?28;') == {}
    assert parse_cookie('name=Dima=User;age=28=Dima;') == {'name': 'Dima=User', 'age': '28=Dima'}
    assert parse_cookie('name=Dima=User=Dima;age//28;') == {'name': 'Dima=User=Dima'}
    assert parse_cookie('name/Dima=User=Dima;age?28;') == {'Dima': 'User=Dima'}
    assert parse_cookie('name/Dima=User=Dima=age=28;') == {'Dima': 'User=Dima=age=28'}
    assert parse_cookie('name/Dima=User&/Dima?age===28;') == {'Dima': 'User'}
