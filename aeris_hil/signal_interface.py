import can
from abc import ABC, abstractmethod

class SignalInterface(ABC):

    @abstractmethod
    def set_signal(self, name: str, value):
        pass

    @abstractmethod
    def get_signal(self, name: str):
        pass

class CANSimulationInterface(SignalInterface):

    def __init__(self):
        self.bus = can.Bus(interface="virtual")

    def set_signal(self, name: str, value):
        msg = can.Message(
            arbitration_id=0x123,
            data=[value],
            is_extended_id=False
        )
        self.bus.send(msg)

    def get_signal(self, name: str):
        msg = self.bus.recv(timeout=1)
        return msg.data if msg else None

