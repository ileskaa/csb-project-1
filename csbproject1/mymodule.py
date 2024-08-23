from django.contrib.auth.hashers import BasePasswordHasher


class FakeHasher(BasePasswordHasher):
    algorithm = "fake_algorithm"

    def encode(self, password, salt):
        # This hasher sucks so much that there is no encoding.
        # It directly returns the password
        return password

    def verify(self, password, encoded):
        # The verification is so broken that it always returns True
        return True

    def safe_summary(self, encoded):
        # Actually, this summary has nothing safe
        return {'foo', 'bar'}
