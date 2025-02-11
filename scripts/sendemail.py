from django.core.mail import EmailMessage
from django.conf import settings

settings.configure(
    EMAIL_HOST='mail.finderskeepers.ai',
    EMAIL_PORT=465,
    EMAIL_HOST_USER='support@finderskeepers.ai',
    EMAIL_HOST_PASSWORD='L4h6b##+g%db',
    EMAIL_USE_SSL=True,  # or EMAIL_USE_TLS = True
)

email = EmailMessage(
    subject='End of Class Notice',
    body='Your class is officially ending today, I wish you goodluck in your tech journey',
    from_email=settings.EMAIL_HOST_USER,
    to=['favouroghenevwoke@gmail.com'],
    bcc=['bcc@anotherbestuser.com'],
    reply_to=['whoever@itmaybe.com'],
)

email.send()
