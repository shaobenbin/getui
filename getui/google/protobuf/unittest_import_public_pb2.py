# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_import_public.proto

from getui.google.protobuf import descriptor as _descriptor
from getui.google.protobuf import message as _message
from getui.google.protobuf import reflection as _reflection
from getui.google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/unittest_import_public.proto',
  package='protobuf_unittest_import',
  serialized_pb='\n,google/protobuf/unittest_import_public.proto\x12\x18protobuf_unittest_import\" \n\x13PublicImportMessage\x12\t\n\x01\x65\x18\x01 \x01(\x05\x42\x1a\n\x18\x63om.google.protobuf.test')




_PUBLICIMPORTMESSAGE = _descriptor.Descriptor(
  name='PublicImportMessage',
  full_name='protobuf_unittest_import.PublicImportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='e', full_name='protobuf_unittest_import.PublicImportMessage.e', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=74,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['PublicImportMessage'] = _PUBLICIMPORTMESSAGE

class PublicImportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PUBLICIMPORTMESSAGE

  # @@protoc_insertion_point(class_scope:protobuf_unittest_import.PublicImportMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\030com.google.protobuf.test')
# @@protoc_insertion_point(module_scope)
