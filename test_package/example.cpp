#include <openssl/ssl.h>
#include <openssl/err.h>

#include "hello/hello.h"

int main() {
    hello();
    OpenSSL_add_all_algorithms();
    ERR_load_BIO_strings();
    ERR_load_crypto_strings();
    SSL_load_error_strings();
}
