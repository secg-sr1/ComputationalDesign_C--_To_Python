from enum import Enum

class Status(Enum):
    InStore = 0
    InTransit = 1
    OutForDelivery = 2
    Delivered = 3


packageStatus = Status.Delivered

print("Package status is: ", packageStatus)

if packageStatus == Status.InStore:
    print("Package hasn't leaved facilities")

elif packageStatus == Status.InTransit:
    print("Package is on its way")

elif packageStatus == Status.OutForDelivery:
    print("You will receive your package VERY soon")

elif packageStatus == Status.Delivered:
    print("Package is delivered")