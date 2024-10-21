from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.crypto import constant_time_compare


class CustomPasswordHasher(BasePasswordHasher):
    # This variable must be defined for the hasher to be valid
    algorithm = "custom"

    def salt(self):
        return ""

    def encode(self, password, salt):
        assert salt == ""
        # The name of the algorithm used to verify the password
        # must be encoded with it
        return 'custom$$%s' % password

    def verify(self, password, encoded):
        encoded_2 = self.encode(password, "")
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self):
        return {'foo', 'bar'}
