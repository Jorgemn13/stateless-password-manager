import click
import hashlib
import pyperclip as pc
import base64

@click.command()
@click.option('--site', '-s', required=True, help='twitter.com')
@click.option('--username', '-u', required=False, help='jorge')
@click.option('--length', '-l', default=12, show_default=True, help="Length of new password")
@click.option('--counter', '-c', default=1, show_default=True, help="The version of the password you are on")
@click.option('--algorithm', '-a', default='BLAKE2', show_default=True,
              type=click.Choice(['BLAKE2'], case_sensitive=False))

def main(length: int = 12, site: str = '', username: str = '', algorithm: str = 'BLAKE2', counter: int = 1):
    """A stateless password manager that can generate passwords on the go. ⚡
        The site parameter is required but a username is optional."""

    password = input('Enter Master Password: ')
    if password:
        password_string = ''.join(filter(None, [site, username, password, str(counter)]))
        return hash_string(length, algorithm, password_string)
    click.secho("Something went wrong 🥴", fg='red', bold=True)


def hash_string(length, algorithm, password_string):
    match algorithm:
        case 'BLAKE2':
            newPass = hashlib.blake2s(password_string.encode(), digest_size=(int(length))).digest()

    base64_string = base64.urlsafe_b64encode(newPass).decode()

    pc.copy(base64_string)
    click.secho('✨ Hashed password: ' + base64_string + ' copied to clipboard ✨', fg='bright_green', bold=True)


if __name__ == '__main__':
    main()