# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs_msg.proto',
  package='com.moon.demo.cs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63s_msg.proto\x12\x10\x63om.moon.demo.cs\x1a\x0c\x63ommon.proto\"\x15\n\x08\x44\x65mo1Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"2\n\x08\x44\x65mo1Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo1Nfy\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x15\n\x08\x44\x65mo3Nfy\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x17\n\nDemo100Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"4\n\nDemo100Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x17\n\nDemo200Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"4\n\nDemo200Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x17\n\nDemo300Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"4\n\nDemo300Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtxb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_DEMO1REQ = _descriptor.Descriptor(
  name='Demo1Req',
  full_name='com.moon.demo.cs.Demo1Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo1Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=69,
)


_DEMO1RSP = _descriptor.Descriptor(
  name='Demo1Rsp',
  full_name='com.moon.demo.cs.Demo1Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.cs.Demo1Rsp.err_ctx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=121,
)


_DEMO1NFY = _descriptor.Descriptor(
  name='Demo1Nfy',
  full_name='com.moon.demo.cs.Demo1Nfy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo1Nfy.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=144,
)


_DEMO3NFY = _descriptor.Descriptor(
  name='Demo3Nfy',
  full_name='com.moon.demo.cs.Demo3Nfy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo3Nfy.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=167,
)


_DEMO100REQ = _descriptor.Descriptor(
  name='Demo100Req',
  full_name='com.moon.demo.cs.Demo100Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo100Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=192,
)


_DEMO100RSP = _descriptor.Descriptor(
  name='Demo100Rsp',
  full_name='com.moon.demo.cs.Demo100Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.cs.Demo100Rsp.err_ctx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=246,
)


_DEMO200REQ = _descriptor.Descriptor(
  name='Demo200Req',
  full_name='com.moon.demo.cs.Demo200Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo200Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=271,
)


_DEMO200RSP = _descriptor.Descriptor(
  name='Demo200Rsp',
  full_name='com.moon.demo.cs.Demo200Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.cs.Demo200Rsp.err_ctx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=325,
)


_DEMO300REQ = _descriptor.Descriptor(
  name='Demo300Req',
  full_name='com.moon.demo.cs.Demo300Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.cs.Demo300Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=350,
)


_DEMO300RSP = _descriptor.Descriptor(
  name='Demo300Rsp',
  full_name='com.moon.demo.cs.Demo300Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.cs.Demo300Rsp.err_ctx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=404,
)

_DEMO1RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO100RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO200RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO300RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
DESCRIPTOR.message_types_by_name['Demo1Req'] = _DEMO1REQ
DESCRIPTOR.message_types_by_name['Demo1Rsp'] = _DEMO1RSP
DESCRIPTOR.message_types_by_name['Demo1Nfy'] = _DEMO1NFY
DESCRIPTOR.message_types_by_name['Demo3Nfy'] = _DEMO3NFY
DESCRIPTOR.message_types_by_name['Demo100Req'] = _DEMO100REQ
DESCRIPTOR.message_types_by_name['Demo100Rsp'] = _DEMO100RSP
DESCRIPTOR.message_types_by_name['Demo200Req'] = _DEMO200REQ
DESCRIPTOR.message_types_by_name['Demo200Rsp'] = _DEMO200RSP
DESCRIPTOR.message_types_by_name['Demo300Req'] = _DEMO300REQ
DESCRIPTOR.message_types_by_name['Demo300Rsp'] = _DEMO300RSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Demo1Req = _reflection.GeneratedProtocolMessageType('Demo1Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO1REQ,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo1Req)
  ))
_sym_db.RegisterMessage(Demo1Req)

Demo1Rsp = _reflection.GeneratedProtocolMessageType('Demo1Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO1RSP,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo1Rsp)
  ))
_sym_db.RegisterMessage(Demo1Rsp)

Demo1Nfy = _reflection.GeneratedProtocolMessageType('Demo1Nfy', (_message.Message,), dict(
  DESCRIPTOR = _DEMO1NFY,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo1Nfy)
  ))
_sym_db.RegisterMessage(Demo1Nfy)

Demo3Nfy = _reflection.GeneratedProtocolMessageType('Demo3Nfy', (_message.Message,), dict(
  DESCRIPTOR = _DEMO3NFY,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo3Nfy)
  ))
_sym_db.RegisterMessage(Demo3Nfy)

Demo100Req = _reflection.GeneratedProtocolMessageType('Demo100Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO100REQ,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo100Req)
  ))
_sym_db.RegisterMessage(Demo100Req)

Demo100Rsp = _reflection.GeneratedProtocolMessageType('Demo100Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO100RSP,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo100Rsp)
  ))
_sym_db.RegisterMessage(Demo100Rsp)

Demo200Req = _reflection.GeneratedProtocolMessageType('Demo200Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO200REQ,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo200Req)
  ))
_sym_db.RegisterMessage(Demo200Req)

Demo200Rsp = _reflection.GeneratedProtocolMessageType('Demo200Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO200RSP,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo200Rsp)
  ))
_sym_db.RegisterMessage(Demo200Rsp)

Demo300Req = _reflection.GeneratedProtocolMessageType('Demo300Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO300REQ,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo300Req)
  ))
_sym_db.RegisterMessage(Demo300Req)

Demo300Rsp = _reflection.GeneratedProtocolMessageType('Demo300Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO300RSP,
  __module__ = 'cs_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.cs.Demo300Rsp)
  ))
_sym_db.RegisterMessage(Demo300Rsp)


# @@protoc_insertion_point(module_scope)
