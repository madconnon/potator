"""Generated by the protocol buffer compiler.  DO NOT EDIT!
source: potator.proto
"""

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: potator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='potator.proto',
  package='potator',
  serialized_pb=_b('\n\rpotator.proto\x12\x07potator\"3\n\x04Ping\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\t\x12\r\n\x05reply\x18\x03 \x02(\x08\"\xae\x01\n\x08OurpData\x12(\n\x04type\x18\x01 \x02(\x0e\x32\x1a.potator.OurpData.OurpType\x12\x11\n\tipAddress\x18\x02 \x02(\t\x12\x10\n\x08onionUrl\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\t\"B\n\x08OurpType\x12\x0b\n\x07REQUEST\x10\x00\x12\t\n\x05REPLY\x10\x01\x12\x0c\n\x08GREETING\x10\x02\x12\x10\n\x0cGREETING_ACK\x10\x03\"2\n\x06IpData\x12\x1a\n\x12\x64\x65stinationAddress\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\"\x9e\x02\n\x05Spore\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12)\n\x08\x64\x61taType\x18\x02 \x02(\x0e\x32\x17.potator.Spore.DataType\x12)\n\x08\x63\x61stType\x18\x03 \x02(\x0e\x32\x17.potator.Spore.CastType\x12#\n\x08ourpData\x18\x04 \x01(\x0b\x32\x11.potator.OurpData\x12\x1f\n\x06ipData\x18\x05 \x01(\x0b\x32\x0f.potator.IpData\x12\x1b\n\x04ping\x18\x06 \x01(\x0b\x32\r.potator.Ping\"&\n\x08\x44\x61taType\x12\x06\n\x02IP\x10\x00\x12\x08\n\x04OURP\x10\x01\x12\x08\n\x04PING\x10\x02\"&\n\x08\x43\x61stType\x12\x0b\n\x07UNICAST\x10\x00\x12\r\n\tBROADCAST\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OURPDATA_OURPTYPE = _descriptor.EnumDescriptor(
  name='OurpType',
  full_name='potator.OurpData.OurpType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREETING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREETING_ACK', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=188,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_OURPDATA_OURPTYPE)

_SPORE_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='potator.Spore.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OURP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=517,
  serialized_end=555,
)
_sym_db.RegisterEnumDescriptor(_SPORE_DATATYPE)

_SPORE_CASTTYPE = _descriptor.EnumDescriptor(
  name='CastType',
  full_name='potator.Spore.CastType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNICAST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=557,
  serialized_end=595,
)
_sym_db.RegisterEnumDescriptor(_SPORE_CASTTYPE)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='potator.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='potator.Ping.source', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='potator.Ping.data', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reply', full_name='potator.Ping.reply', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=77,
)


_OURPDATA = _descriptor.Descriptor(
  name='OurpData',
  full_name='potator.OurpData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='potator.OurpData.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipAddress', full_name='potator.OurpData.ipAddress', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='onionUrl', full_name='potator.OurpData.onionUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='potator.OurpData.payload', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OURPDATA_OURPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=254,
)


_IPDATA = _descriptor.Descriptor(
  name='IpData',
  full_name='potator.IpData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destinationAddress', full_name='potator.IpData.destinationAddress', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='potator.IpData.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=306,
)


_SPORE = _descriptor.Descriptor(
  name='Spore',
  full_name='potator.Spore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='potator.Spore.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='potator.Spore.dataType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='castType', full_name='potator.Spore.castType', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ourpData', full_name='potator.Spore.ourpData', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipData', full_name='potator.Spore.ipData', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='potator.Spore.ping', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SPORE_DATATYPE,
    _SPORE_CASTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=595,
)

_OURPDATA.fields_by_name['type'].enum_type = _OURPDATA_OURPTYPE
_OURPDATA_OURPTYPE.containing_type = _OURPDATA
_SPORE.fields_by_name['dataType'].enum_type = _SPORE_DATATYPE
_SPORE.fields_by_name['castType'].enum_type = _SPORE_CASTTYPE
_SPORE.fields_by_name['ourpData'].message_type = _OURPDATA
_SPORE.fields_by_name['ipData'].message_type = _IPDATA
_SPORE.fields_by_name['ping'].message_type = _PING
_SPORE_DATATYPE.containing_type = _SPORE
_SPORE_CASTTYPE.containing_type = _SPORE
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['OurpData'] = _OURPDATA
DESCRIPTOR.message_types_by_name['IpData'] = _IPDATA
DESCRIPTOR.message_types_by_name['Spore'] = _SPORE

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'potator_pb2'
  # @@protoc_insertion_point(class_scope:potator.Ping)
  ))
_sym_db.RegisterMessage(Ping)

OurpData = _reflection.GeneratedProtocolMessageType('OurpData', (_message.Message,), dict(
  DESCRIPTOR = _OURPDATA,
  __module__ = 'potator_pb2'
  # @@protoc_insertion_point(class_scope:potator.OurpData)
  ))
_sym_db.RegisterMessage(OurpData)

IpData = _reflection.GeneratedProtocolMessageType('IpData', (_message.Message,), dict(
  DESCRIPTOR = _IPDATA,
  __module__ = 'potator_pb2'
  # @@protoc_insertion_point(class_scope:potator.IpData)
  ))
_sym_db.RegisterMessage(IpData)

Spore = _reflection.GeneratedProtocolMessageType('Spore', (_message.Message,), dict(
  DESCRIPTOR = _SPORE,
  __module__ = 'potator_pb2'
  # @@protoc_insertion_point(class_scope:potator.Spore)
  ))
_sym_db.RegisterMessage(Spore)


# @@protoc_insertion_point(module_scope)
