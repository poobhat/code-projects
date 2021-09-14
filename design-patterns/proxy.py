import time
class Producer:

    """Instantiation of this class is resource-intensive"""
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer is ready to meet the guests now")

class Proxy:
    """This a proxy for the resource-intensive object as a middleman"""
    def __init__(self):
        self.producer = None
        self.occupied = 'No'

    def produce(self):
        """Check if resource is available"""
        print("Artist is checking if the producer is available")
        if self.occupied == 'No':
            # If producer is available, create a producer object
            self.producer = Producer()
            time.sleep(4)
            # Make the producer meet the guest
            self.producer.meet()
        else:
            # Otherwise don't instantiate the producer
            time.sleep(4)
            print("Producer is busy")

# Instantiate a proxy
p = Proxy()
# # Make the proxy(artist) producer until the producer is available
# p.produce()
# Change the status of the Producer
p.occupied = 'Yes'
# Make the producer produce
p.produce()
