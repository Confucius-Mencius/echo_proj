// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: ss_msg_id.proto

package com.moon.demo.ss;

public final class SsMsgId {
  private SsMsgId() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  /**
   * Protobuf enum {@code com.moon.demo.ss.MsgID}
   */
  public enum MsgID
      implements com.google.protobuf.ProtocolMessageEnum {
    /**
     * <code>PLACE_HOLDER = 0;</code>
     */
    PLACE_HOLDER(0),
    /**
     * <code>MSG_ID_GLOBAL_REQ = 2000;</code>
     */
    MSG_ID_GLOBAL_REQ(2000),
    /**
     * <code>MSG_ID_GLOBAL_RSP = 2001;</code>
     */
    MSG_ID_GLOBAL_RSP(2001),
    /**
     * <code>MSG_ID_DEMO_1_REQ = 2002;</code>
     */
    MSG_ID_DEMO_1_REQ(2002),
    /**
     * <code>MSG_ID_DEMO_1_RSP = 2003;</code>
     */
    MSG_ID_DEMO_1_RSP(2003),
    /**
     * <code>MSG_ID_DEMO_1_NFY = 2004;</code>
     */
    MSG_ID_DEMO_1_NFY(2004),
    UNRECOGNIZED(-1),
    ;

    /**
     * <code>PLACE_HOLDER = 0;</code>
     */
    public static final int PLACE_HOLDER_VALUE = 0;
    /**
     * <code>MSG_ID_GLOBAL_REQ = 2000;</code>
     */
    public static final int MSG_ID_GLOBAL_REQ_VALUE = 2000;
    /**
     * <code>MSG_ID_GLOBAL_RSP = 2001;</code>
     */
    public static final int MSG_ID_GLOBAL_RSP_VALUE = 2001;
    /**
     * <code>MSG_ID_DEMO_1_REQ = 2002;</code>
     */
    public static final int MSG_ID_DEMO_1_REQ_VALUE = 2002;
    /**
     * <code>MSG_ID_DEMO_1_RSP = 2003;</code>
     */
    public static final int MSG_ID_DEMO_1_RSP_VALUE = 2003;
    /**
     * <code>MSG_ID_DEMO_1_NFY = 2004;</code>
     */
    public static final int MSG_ID_DEMO_1_NFY_VALUE = 2004;


    public final int getNumber() {
      if (this == UNRECOGNIZED) {
        throw new java.lang.IllegalArgumentException(
            "Can't get the number of an unknown enum value.");
      }
      return value;
    }

    /**
     * @deprecated Use {@link #forNumber(int)} instead.
     */
    @java.lang.Deprecated
    public static MsgID valueOf(int value) {
      return forNumber(value);
    }

    public static MsgID forNumber(int value) {
      switch (value) {
        case 0: return PLACE_HOLDER;
        case 2000: return MSG_ID_GLOBAL_REQ;
        case 2001: return MSG_ID_GLOBAL_RSP;
        case 2002: return MSG_ID_DEMO_1_REQ;
        case 2003: return MSG_ID_DEMO_1_RSP;
        case 2004: return MSG_ID_DEMO_1_NFY;
        default: return null;
      }
    }

    public static com.google.protobuf.Internal.EnumLiteMap<MsgID>
        internalGetValueMap() {
      return internalValueMap;
    }
    private static final com.google.protobuf.Internal.EnumLiteMap<
        MsgID> internalValueMap =
          new com.google.protobuf.Internal.EnumLiteMap<MsgID>() {
            public MsgID findValueByNumber(int number) {
              return MsgID.forNumber(number);
            }
          };

    public final com.google.protobuf.Descriptors.EnumValueDescriptor
        getValueDescriptor() {
      return getDescriptor().getValues().get(ordinal());
    }
    public final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptorForType() {
      return getDescriptor();
    }
    public static final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptor() {
      return com.moon.demo.ss.SsMsgId.getDescriptor().getEnumTypes().get(0);
    }

    private static final MsgID[] VALUES = values();

    public static MsgID valueOf(
        com.google.protobuf.Descriptors.EnumValueDescriptor desc) {
      if (desc.getType() != getDescriptor()) {
        throw new java.lang.IllegalArgumentException(
          "EnumValueDescriptor is not for this type.");
      }
      if (desc.getIndex() == -1) {
        return UNRECOGNIZED;
      }
      return VALUES[desc.getIndex()];
    }

    private final int value;

    private MsgID(int value) {
      this.value = value;
    }

    // @@protoc_insertion_point(enum_scope:com.moon.demo.ss.MsgID)
  }


  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\017ss_msg_id.proto\022\020com.moon.demo.ss*\221\001\n\005" +
      "MsgID\022\020\n\014PLACE_HOLDER\020\000\022\026\n\021MSG_ID_GLOBAL" +
      "_REQ\020\320\017\022\026\n\021MSG_ID_GLOBAL_RSP\020\321\017\022\026\n\021MSG_I" +
      "D_DEMO_1_REQ\020\322\017\022\026\n\021MSG_ID_DEMO_1_RSP\020\323\017\022" +
      "\026\n\021MSG_ID_DEMO_1_NFY\020\324\017b\006proto3"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
        new com.google.protobuf.Descriptors.FileDescriptor.    InternalDescriptorAssigner() {
          public com.google.protobuf.ExtensionRegistry assignDescriptors(
              com.google.protobuf.Descriptors.FileDescriptor root) {
            descriptor = root;
            return null;
          }
        };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
  }

  // @@protoc_insertion_point(outer_class_scope)
}