from django.contrib.auth.hashers import BasePasswordHasher


class CustomHasher(BasePasswordHasher):
    # This variable must be defined for the hasher to be valid
    algorithm = "no_algorithm"

    def encode(self, password, salt):
        print('Salt:', salt)
        # There is actually no encoding.
        # It directly returns the password
        return password

    def verify(self):
        # The verification is absent
        return True

    def safe_summary(self):
        # Actually, this summary has nothing safe
        return {'foo', 'bar'}
