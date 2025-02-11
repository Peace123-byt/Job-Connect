from django.dispatch import receiver
from core_root_api.signals import order_created

@receiver(order_created)
def handle_order_created(sender, user, **kwargs):
    print(f"✅ Signal Triggered: Order created by {user.username}")