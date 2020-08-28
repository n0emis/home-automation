from ldif import LDIFParser,LDIFWriter
import base64
import jinja2

parser = LDIFParser(open("/tmp/NOEMIS-ME-userRoot.ldif", 'rb'))
users = []

for k,v in parser.parse():
    users.append({
        'uid': v['uid'][0],
        'pwhash': base64.b64encode(v['userPassword'][0].encode("UTF-8")).decode("UTF-8"),
        'nthash': v['ipaNTHash'][0].hex(),
        'sn': v['sn'][0],
        'cn': v['givenName'][0],
        'mail': v['mail'][0]
    })

template = jinja2.Template(open('ldif.j2').read())

print(template.render(users=users))


