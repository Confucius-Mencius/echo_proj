# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ss_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ss_msg.proto',
  package='com.moon.demo.ss',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0css_msg.proto\x12\x10\x63om.moon.demo.ss\x1a\x0c\x63ommon.proto\"3\n\x08\x44\x65mo2Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x1c\n\x14proto_tcp_thread_idx\x18\x02 \x01(\x05\"2\n\x08\x44\x65mo2Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo3Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"2\n\x08\x44\x65mo3Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"a\n\x08\x44\x65mo4Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x03\x12\t\n\x01\x63\x18\x03 \x01(\t\x12\t\n\x01\x64\x18\x04 \x01(\x0c\x12)\n\x04\x66lag\x18\x05 \x01(\x0e\x32\x1b.com.moon.demo.ss.Demo4Flag\"2\n\x08\x44\x65mo4Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\".\n\x08\x44\x65mo5Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x17\n\x0fwork_thread_idx\x18\x02 \x01(\x05\"2\n\x08\x44\x65mo5Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo6Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"2\n\x08\x44\x65mo6Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo7Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"2\n\x08\x44\x65mo7Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo8Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"2\n\x08\x44\x65mo8Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"0\n\x08\x44\x65mo9Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\x19\n\x11\x62urden_thread_idx\x18\x02 \x01(\x05\"2\n\x08\x44\x65mo9Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x16\n\tDemo10Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"3\n\tDemo10Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x16\n\tDemo20Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"3\n\tDemo20Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x16\n\tDemo50Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"3\n\tDemo50Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x16\n\tDemo90Req\x12\t\n\x01\x61\x18\x01 \x01(\x05\"3\n\tDemo90Rsp\x12&\n\x07\x65rr_ctx\x18\x01 \x01(\x0b\x32\x15.com.moon.demo.ErrCtx\"\x15\n\x08\x44\x65mo2Nfy\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x15\n\x08\x44\x65mo5Nfy\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x15\n\x08\x44\x65mo9Nfy\x12\t\n\x01\x61\x18\x01 \x01(\x05*a\n\tDemo4Flag\x12\x13\n\x0f\x44\x45MO_4_FLAG_MIN\x10\x00\x12\x12\n\x0e\x44\x45MO_4_FLAG_XX\x10\x00\x12\x12\n\x0e\x44\x45MO_4_FLAG_YY\x10\x01\x12\x13\n\x0f\x44\x45MO_4_FLAG_MAX\x10\x02\x1a\x02\x10\x01\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_DEMO4FLAG = _descriptor.EnumDescriptor(
  name='Demo4Flag',
  full_name='com.moon.demo.ss.Demo4Flag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEMO_4_FLAG_MIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEMO_4_FLAG_XX', index=1, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEMO_4_FLAG_YY', index=2, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEMO_4_FLAG_MAX', index=3, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=1183,
  serialized_end=1280,
)
_sym_db.RegisterEnumDescriptor(_DEMO4FLAG)

Demo4Flag = enum_type_wrapper.EnumTypeWrapper(_DEMO4FLAG)
DEMO_4_FLAG_MIN = 0
DEMO_4_FLAG_XX = 0
DEMO_4_FLAG_YY = 1
DEMO_4_FLAG_MAX = 2



_DEMO2REQ = _descriptor.Descriptor(
  name='Demo2Req',
  full_name='com.moon.demo.ss.Demo2Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo2Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_tcp_thread_idx', full_name='com.moon.demo.ss.Demo2Req.proto_tcp_thread_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_end=99,
)


_DEMO2RSP = _descriptor.Descriptor(
  name='Demo2Rsp',
  full_name='com.moon.demo.ss.Demo2Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo2Rsp.err_ctx', index=0,
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
  serialized_start=101,
  serialized_end=151,
)


_DEMO3REQ = _descriptor.Descriptor(
  name='Demo3Req',
  full_name='com.moon.demo.ss.Demo3Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo3Req.a', index=0,
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
  serialized_start=153,
  serialized_end=174,
)


_DEMO3RSP = _descriptor.Descriptor(
  name='Demo3Rsp',
  full_name='com.moon.demo.ss.Demo3Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo3Rsp.err_ctx', index=0,
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
  serialized_start=176,
  serialized_end=226,
)


_DEMO4REQ = _descriptor.Descriptor(
  name='Demo4Req',
  full_name='com.moon.demo.ss.Demo4Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo4Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='com.moon.demo.ss.Demo4Req.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='c', full_name='com.moon.demo.ss.Demo4Req.c', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='com.moon.demo.ss.Demo4Req.d', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flag', full_name='com.moon.demo.ss.Demo4Req.flag', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=228,
  serialized_end=325,
)


_DEMO4RSP = _descriptor.Descriptor(
  name='Demo4Rsp',
  full_name='com.moon.demo.ss.Demo4Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo4Rsp.err_ctx', index=0,
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
  serialized_start=327,
  serialized_end=377,
)


_DEMO5REQ = _descriptor.Descriptor(
  name='Demo5Req',
  full_name='com.moon.demo.ss.Demo5Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo5Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_thread_idx', full_name='com.moon.demo.ss.Demo5Req.work_thread_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=379,
  serialized_end=425,
)


_DEMO5RSP = _descriptor.Descriptor(
  name='Demo5Rsp',
  full_name='com.moon.demo.ss.Demo5Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo5Rsp.err_ctx', index=0,
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
  serialized_start=427,
  serialized_end=477,
)


_DEMO6REQ = _descriptor.Descriptor(
  name='Demo6Req',
  full_name='com.moon.demo.ss.Demo6Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo6Req.a', index=0,
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
  serialized_start=479,
  serialized_end=500,
)


_DEMO6RSP = _descriptor.Descriptor(
  name='Demo6Rsp',
  full_name='com.moon.demo.ss.Demo6Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo6Rsp.err_ctx', index=0,
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
  serialized_start=502,
  serialized_end=552,
)


_DEMO7REQ = _descriptor.Descriptor(
  name='Demo7Req',
  full_name='com.moon.demo.ss.Demo7Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo7Req.a', index=0,
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
  serialized_start=554,
  serialized_end=575,
)


_DEMO7RSP = _descriptor.Descriptor(
  name='Demo7Rsp',
  full_name='com.moon.demo.ss.Demo7Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo7Rsp.err_ctx', index=0,
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
  serialized_start=577,
  serialized_end=627,
)


_DEMO8REQ = _descriptor.Descriptor(
  name='Demo8Req',
  full_name='com.moon.demo.ss.Demo8Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo8Req.a', index=0,
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
  serialized_start=629,
  serialized_end=650,
)


_DEMO8RSP = _descriptor.Descriptor(
  name='Demo8Rsp',
  full_name='com.moon.demo.ss.Demo8Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo8Rsp.err_ctx', index=0,
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
  serialized_start=652,
  serialized_end=702,
)


_DEMO9REQ = _descriptor.Descriptor(
  name='Demo9Req',
  full_name='com.moon.demo.ss.Demo9Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo9Req.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='burden_thread_idx', full_name='com.moon.demo.ss.Demo9Req.burden_thread_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=704,
  serialized_end=752,
)


_DEMO9RSP = _descriptor.Descriptor(
  name='Demo9Rsp',
  full_name='com.moon.demo.ss.Demo9Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo9Rsp.err_ctx', index=0,
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
  serialized_start=754,
  serialized_end=804,
)


_DEMO10REQ = _descriptor.Descriptor(
  name='Demo10Req',
  full_name='com.moon.demo.ss.Demo10Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo10Req.a', index=0,
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
  serialized_start=806,
  serialized_end=828,
)


_DEMO10RSP = _descriptor.Descriptor(
  name='Demo10Rsp',
  full_name='com.moon.demo.ss.Demo10Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo10Rsp.err_ctx', index=0,
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
  serialized_start=830,
  serialized_end=881,
)


_DEMO20REQ = _descriptor.Descriptor(
  name='Demo20Req',
  full_name='com.moon.demo.ss.Demo20Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo20Req.a', index=0,
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
  serialized_start=883,
  serialized_end=905,
)


_DEMO20RSP = _descriptor.Descriptor(
  name='Demo20Rsp',
  full_name='com.moon.demo.ss.Demo20Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo20Rsp.err_ctx', index=0,
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
  serialized_start=907,
  serialized_end=958,
)


_DEMO50REQ = _descriptor.Descriptor(
  name='Demo50Req',
  full_name='com.moon.demo.ss.Demo50Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo50Req.a', index=0,
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
  serialized_start=960,
  serialized_end=982,
)


_DEMO50RSP = _descriptor.Descriptor(
  name='Demo50Rsp',
  full_name='com.moon.demo.ss.Demo50Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo50Rsp.err_ctx', index=0,
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
  serialized_start=984,
  serialized_end=1035,
)


_DEMO90REQ = _descriptor.Descriptor(
  name='Demo90Req',
  full_name='com.moon.demo.ss.Demo90Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo90Req.a', index=0,
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
  serialized_start=1037,
  serialized_end=1059,
)


_DEMO90RSP = _descriptor.Descriptor(
  name='Demo90Rsp',
  full_name='com.moon.demo.ss.Demo90Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_ctx', full_name='com.moon.demo.ss.Demo90Rsp.err_ctx', index=0,
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
  serialized_start=1061,
  serialized_end=1112,
)


_DEMO2NFY = _descriptor.Descriptor(
  name='Demo2Nfy',
  full_name='com.moon.demo.ss.Demo2Nfy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo2Nfy.a', index=0,
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
  serialized_start=1114,
  serialized_end=1135,
)


_DEMO5NFY = _descriptor.Descriptor(
  name='Demo5Nfy',
  full_name='com.moon.demo.ss.Demo5Nfy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo5Nfy.a', index=0,
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
  serialized_start=1137,
  serialized_end=1158,
)


_DEMO9NFY = _descriptor.Descriptor(
  name='Demo9Nfy',
  full_name='com.moon.demo.ss.Demo9Nfy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='com.moon.demo.ss.Demo9Nfy.a', index=0,
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
  serialized_start=1160,
  serialized_end=1181,
)

_DEMO2RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO3RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO4REQ.fields_by_name['flag'].enum_type = _DEMO4FLAG
_DEMO4RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO5RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO6RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO7RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO8RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO9RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO10RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO20RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO50RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
_DEMO90RSP.fields_by_name['err_ctx'].message_type = common__pb2._ERRCTX
DESCRIPTOR.message_types_by_name['Demo2Req'] = _DEMO2REQ
DESCRIPTOR.message_types_by_name['Demo2Rsp'] = _DEMO2RSP
DESCRIPTOR.message_types_by_name['Demo3Req'] = _DEMO3REQ
DESCRIPTOR.message_types_by_name['Demo3Rsp'] = _DEMO3RSP
DESCRIPTOR.message_types_by_name['Demo4Req'] = _DEMO4REQ
DESCRIPTOR.message_types_by_name['Demo4Rsp'] = _DEMO4RSP
DESCRIPTOR.message_types_by_name['Demo5Req'] = _DEMO5REQ
DESCRIPTOR.message_types_by_name['Demo5Rsp'] = _DEMO5RSP
DESCRIPTOR.message_types_by_name['Demo6Req'] = _DEMO6REQ
DESCRIPTOR.message_types_by_name['Demo6Rsp'] = _DEMO6RSP
DESCRIPTOR.message_types_by_name['Demo7Req'] = _DEMO7REQ
DESCRIPTOR.message_types_by_name['Demo7Rsp'] = _DEMO7RSP
DESCRIPTOR.message_types_by_name['Demo8Req'] = _DEMO8REQ
DESCRIPTOR.message_types_by_name['Demo8Rsp'] = _DEMO8RSP
DESCRIPTOR.message_types_by_name['Demo9Req'] = _DEMO9REQ
DESCRIPTOR.message_types_by_name['Demo9Rsp'] = _DEMO9RSP
DESCRIPTOR.message_types_by_name['Demo10Req'] = _DEMO10REQ
DESCRIPTOR.message_types_by_name['Demo10Rsp'] = _DEMO10RSP
DESCRIPTOR.message_types_by_name['Demo20Req'] = _DEMO20REQ
DESCRIPTOR.message_types_by_name['Demo20Rsp'] = _DEMO20RSP
DESCRIPTOR.message_types_by_name['Demo50Req'] = _DEMO50REQ
DESCRIPTOR.message_types_by_name['Demo50Rsp'] = _DEMO50RSP
DESCRIPTOR.message_types_by_name['Demo90Req'] = _DEMO90REQ
DESCRIPTOR.message_types_by_name['Demo90Rsp'] = _DEMO90RSP
DESCRIPTOR.message_types_by_name['Demo2Nfy'] = _DEMO2NFY
DESCRIPTOR.message_types_by_name['Demo5Nfy'] = _DEMO5NFY
DESCRIPTOR.message_types_by_name['Demo9Nfy'] = _DEMO9NFY
DESCRIPTOR.enum_types_by_name['Demo4Flag'] = _DEMO4FLAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Demo2Req = _reflection.GeneratedProtocolMessageType('Demo2Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO2REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo2Req)
  ))
_sym_db.RegisterMessage(Demo2Req)

Demo2Rsp = _reflection.GeneratedProtocolMessageType('Demo2Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO2RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo2Rsp)
  ))
_sym_db.RegisterMessage(Demo2Rsp)

Demo3Req = _reflection.GeneratedProtocolMessageType('Demo3Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO3REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo3Req)
  ))
_sym_db.RegisterMessage(Demo3Req)

Demo3Rsp = _reflection.GeneratedProtocolMessageType('Demo3Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO3RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo3Rsp)
  ))
_sym_db.RegisterMessage(Demo3Rsp)

Demo4Req = _reflection.GeneratedProtocolMessageType('Demo4Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO4REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo4Req)
  ))
_sym_db.RegisterMessage(Demo4Req)

Demo4Rsp = _reflection.GeneratedProtocolMessageType('Demo4Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO4RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo4Rsp)
  ))
_sym_db.RegisterMessage(Demo4Rsp)

Demo5Req = _reflection.GeneratedProtocolMessageType('Demo5Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO5REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo5Req)
  ))
_sym_db.RegisterMessage(Demo5Req)

Demo5Rsp = _reflection.GeneratedProtocolMessageType('Demo5Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO5RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo5Rsp)
  ))
_sym_db.RegisterMessage(Demo5Rsp)

Demo6Req = _reflection.GeneratedProtocolMessageType('Demo6Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO6REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo6Req)
  ))
_sym_db.RegisterMessage(Demo6Req)

Demo6Rsp = _reflection.GeneratedProtocolMessageType('Demo6Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO6RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo6Rsp)
  ))
_sym_db.RegisterMessage(Demo6Rsp)

Demo7Req = _reflection.GeneratedProtocolMessageType('Demo7Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO7REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo7Req)
  ))
_sym_db.RegisterMessage(Demo7Req)

Demo7Rsp = _reflection.GeneratedProtocolMessageType('Demo7Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO7RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo7Rsp)
  ))
_sym_db.RegisterMessage(Demo7Rsp)

Demo8Req = _reflection.GeneratedProtocolMessageType('Demo8Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO8REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo8Req)
  ))
_sym_db.RegisterMessage(Demo8Req)

Demo8Rsp = _reflection.GeneratedProtocolMessageType('Demo8Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO8RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo8Rsp)
  ))
_sym_db.RegisterMessage(Demo8Rsp)

Demo9Req = _reflection.GeneratedProtocolMessageType('Demo9Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO9REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo9Req)
  ))
_sym_db.RegisterMessage(Demo9Req)

Demo9Rsp = _reflection.GeneratedProtocolMessageType('Demo9Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO9RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo9Rsp)
  ))
_sym_db.RegisterMessage(Demo9Rsp)

Demo10Req = _reflection.GeneratedProtocolMessageType('Demo10Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO10REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo10Req)
  ))
_sym_db.RegisterMessage(Demo10Req)

Demo10Rsp = _reflection.GeneratedProtocolMessageType('Demo10Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO10RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo10Rsp)
  ))
_sym_db.RegisterMessage(Demo10Rsp)

Demo20Req = _reflection.GeneratedProtocolMessageType('Demo20Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO20REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo20Req)
  ))
_sym_db.RegisterMessage(Demo20Req)

Demo20Rsp = _reflection.GeneratedProtocolMessageType('Demo20Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO20RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo20Rsp)
  ))
_sym_db.RegisterMessage(Demo20Rsp)

Demo50Req = _reflection.GeneratedProtocolMessageType('Demo50Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO50REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo50Req)
  ))
_sym_db.RegisterMessage(Demo50Req)

Demo50Rsp = _reflection.GeneratedProtocolMessageType('Demo50Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO50RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo50Rsp)
  ))
_sym_db.RegisterMessage(Demo50Rsp)

Demo90Req = _reflection.GeneratedProtocolMessageType('Demo90Req', (_message.Message,), dict(
  DESCRIPTOR = _DEMO90REQ,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo90Req)
  ))
_sym_db.RegisterMessage(Demo90Req)

Demo90Rsp = _reflection.GeneratedProtocolMessageType('Demo90Rsp', (_message.Message,), dict(
  DESCRIPTOR = _DEMO90RSP,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo90Rsp)
  ))
_sym_db.RegisterMessage(Demo90Rsp)

Demo2Nfy = _reflection.GeneratedProtocolMessageType('Demo2Nfy', (_message.Message,), dict(
  DESCRIPTOR = _DEMO2NFY,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo2Nfy)
  ))
_sym_db.RegisterMessage(Demo2Nfy)

Demo5Nfy = _reflection.GeneratedProtocolMessageType('Demo5Nfy', (_message.Message,), dict(
  DESCRIPTOR = _DEMO5NFY,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo5Nfy)
  ))
_sym_db.RegisterMessage(Demo5Nfy)

Demo9Nfy = _reflection.GeneratedProtocolMessageType('Demo9Nfy', (_message.Message,), dict(
  DESCRIPTOR = _DEMO9NFY,
  __module__ = 'ss_msg_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ss.Demo9Nfy)
  ))
_sym_db.RegisterMessage(Demo9Nfy)


_DEMO4FLAG._options = None
# @@protoc_insertion_point(module_scope)
