# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import services.room_manager_pb2 as room__manager__pb2


class RoomManagerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/room.RoomManager/Register',
                request_serializer=room__manager__pb2.Room.SerializeToString,
                response_deserializer=room__manager__pb2.Result.FromString,
                )
        self.Signin = channel.unary_unary(
                '/room.RoomManager/Signin',
                request_serializer=room__manager__pb2.Room.SerializeToString,
                response_deserializer=room__manager__pb2.Result.FromString,
                )


class RoomManagerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Signin(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoomManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=room__manager__pb2.Room.FromString,
                    response_serializer=room__manager__pb2.Result.SerializeToString,
            ),
            'Signin': grpc.unary_unary_rpc_method_handler(
                    servicer.Signin,
                    request_deserializer=room__manager__pb2.Room.FromString,
                    response_serializer=room__manager__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'room.RoomManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoomManager(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/room.RoomManager/Register',
            room__manager__pb2.Room.SerializeToString,
            room__manager__pb2.Result.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Signin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/room.RoomManager/Signin',
            room__manager__pb2.Room.SerializeToString,
            room__manager__pb2.Result.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
