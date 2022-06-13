def parse(query: str) -> dict:
    if '?' not in query:
        return {}
    else:
        no_need, needed = query.split('?')
        refactor = [i.split('=', 1) for i in needed.split('&')]
        parsed_dict = {val[0]: val[1] for val in refactor if len(val[0]) and len(val[1]) > 1}
    return parsed_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page:name=ferret:color=purple') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=') == {'name': 'ferret'}
    assert parse('http://example.com/?&name=Dima=') == {'name': 'Dima='}
    assert parse('http://example.com/?&Dima/name=Dima') == {'Dima/name': 'Dima'}
    assert parse('https://example.com/path/to/page:ferret/color:purple&name') == {}
    assert parse('https://example.com/path/to/?:color/=purple&&color=purple') == {':color/': 'purple', 'color': 'purple'}
    assert parse('http://example.com/?&=:;') == {}
    assert parse('http://example.com/?Dima=name/color=&=purple/') == {'Dima': 'name/color='}
    assert parse('https://example.com/path/to/?:color/=purple==color/purlple') == {':color/': 'purple==color/purlple'}
    assert parse('https://example.com/path/to/page?name=ferret=color=') == {'name': 'ferret=color='}


def parse_cookie(query: str) -> dict:
    refactor = [i.split('=', 1) for i in query.split(';')]
    parsed_cookie = {val[0]: val[1] for val in refactor if len(val) > 1}
    return parsed_cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima//age==28;') == {'name': 'Dima//age==28'}
    assert parse_cookie('name==Dima//age==28;') == {'name': '=Dima//age==28'}
    assert parse_cookie('name=/Dima;age=28;') == {'name': '/Dima', 'age': '28'}
    assert parse_cookie('name===Dima/User;age=28;') == {'name': '==Dima/User', 'age': '28'}
    assert parse_cookie('name/Dima:User;age?28;') == {}
    assert parse_cookie('name=Dima=User;age=28=Dima;') == {'name': 'Dima=User', 'age': '28=Dima'}
    assert parse_cookie('name=Dima=User=Dima;age//28;') == {'name': 'Dima=User=Dima'}
    assert parse_cookie('name/Dima=User=Dima;age?28;') == {'name/Dima': 'User=Dima'}
    assert parse_cookie('name/Dima=User=Dima=age=28;') == {'name/Dima': 'User=Dima=age=28'}
    assert parse_cookie('name/Dima=User&/Dima?age===28;') == {'name/Dima': 'User&/Dima?age===28'}
