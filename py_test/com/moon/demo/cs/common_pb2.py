# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='com.moon.demo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\rcom.moon.demo\"+\n\x06\x45rrCtx\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\tb\x06proto3')
)




_ERRCTX = _descriptor.Descriptor(
  name='ErrCtx',
  full_name='com.moon.demo.ErrCtx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='com.moon.demo.ErrCtx.err_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='com.moon.demo.ErrCtx.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=31,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['ErrCtx'] = _ERRCTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrCtx = _reflection.GeneratedProtocolMessageType('ErrCtx', (_message.Message,), dict(
  DESCRIPTOR = _ERRCTX,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:com.moon.demo.ErrCtx)
  ))
_sym_db.RegisterMessage(ErrCtx)


# @@protoc_insertion_point(module_scope)