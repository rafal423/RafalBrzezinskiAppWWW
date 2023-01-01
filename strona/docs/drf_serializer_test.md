from polls.models import Osoba
from polls.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
osoba = Osoba(imie="Adam", nazwisko="Kowalski", miesiac_urodzenia=1)
osoba.save()
serializer = OsobaSerializer(osoba)
serializer.data
{'id': 1, 'imie': 'Adam', 'nazwisko': 'Kowalski', 'miesiac_urodzenia': 1, 'druzyna': None}
content = JSONRenderer().render(serializer.data)
content
b'{"id":1,"imie":"Adam","nazwisko":"Kowalski","miesiac_urodzenia":1,"druzyna":null}'
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = OsobaSerializer(data=data)
deserializer.is_valid()
True
deserializer.validated_data
OrderedDict([('imie', 'Adam'), ('nazwisko', 'Kowalski'), ('miesiac_urodzenia', 1), ('druzyna', None)])
deserializer.save()
<Osoba: Adam Kowalski>
deserializer.data
{'id': 2, 'imie': 'Adam', 'nazwisko': 'Kowalski', 'miesiac_urodzenia': 1, 'druzyna': None}

