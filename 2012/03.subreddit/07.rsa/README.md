# RSA Puzzle

Those who received an email got the following message. Everyone received a different `n` for the puzzle.

<details>
    <summary>3301 Email</summary>

```
    
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1


This message will only be displayed once.

Here is a message that has been encrypted with RSA (the Crypt::RSA Perl module available in CPAN) :

- -----BEGIN COMPRESSED RSA ENCRYPTED MESSAGE-----
Version: 1.99
Scheme: Crypt::RSA::ES::OAEP

eJwBzQAy/zEwADE4OABDeXBoZXJ0ZXh0B4KeBtKjJ7hGKC7/zqyzxUoFDTzRuU4+TLFUrw9qDGjk
YI3fjyMn3G/w9WcfkZMGHdGRicbpTsDO3/oqmVtZpmIDY2HPOeWIZChuLfMDwT3FTUkDjQpsq390
OJ90pArd1JRxdIZtnCvnVy/vg+1MjAFH3ta+CuAwHsIY/3lGOKTin1+5M30BKh7NOQMmBcJ8/RuL
TfXMGQT01QVMeAGq6vORk3iw39KOLRU3Lcn1804G1/zd2mdFWvEMaTbu/F+7
=0KfiT9PUe6QkwJXoM36Ukw==
- -----END COMPRESSED RSA ENCRYPTED MESSAGE-----


Here is the public key used to encrypt it. Note that it has a low bit modulus and is therefore breakable:

$VAR1 = bless( {
                 'e' => 65537,
                 'n' => '7467492769579356967270197440403790283193525917787433197231759008957255433116469460882489015469125000179524189783',
                 'Version' => '1.99',
                 'Identity' => 
               }, 'Crypt::RSA::Key::Public' );


The encrypted message is a number.  Break the decryption key, then come back to this same URL and enter the 
decrypted message to continue.  Each person who has come this far has received a unique message encrypted 
with a unique key.  You are not to collaborate.  Sharing your message or key will result in not receiving 
the next step.

There is a second chance to get your own RSA message and key.  Follow the "Numbers dot TK" hint to find it.

There are many fake messages out there.  Only messages signed with public key ID 7A35090F are valid.  

Good luck.

3301 

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.11 (GNU/Linux)

iQIcBAEBAgAGBQJPEi5PAAoJEBgfAeV6NQkPV58P/0vBho7MrgWy4V4v2CGcq3gU
OfNQ+k/z3TRvJZamGqM0bJbYgaHyG6mekf4v7o68b6v7Riir3maljP0snKV6Wv6j
Ea8tzLZGonrgIJSSH4Ri3Ce9JiX4FGgNf8kY/3MahW5+TPoJGOmugfAf51XrUafH
xTGK6aa9VQoQgg4Hxig8+BQAcNOGBvrnLu2MX4e+K8877YzNhymPNQGiKa/vm/gv
BZN8S5tP9JYbSxZIU9EY5/Ny1c7Rb4uWJfmVm0EuKhx4gnVTuo7DXmZh0bcSmgk+
BPsg/mLdFVKMNaf8Znam4Lg7oGby6fg7duwNcRBtH242oDZi7Ar2PaULDeaEhVS9
Z29zFPGNpwDc8E7hecbfBzlLARkiMOApgORfBeTVP7c3p38efg+24v7Rp26J61Qf
qtppmijeO+BuytVm8XlmGLoMvL8NlCx/9ghTnaQN1hBWT/WpCPRCLC0F982zvfzC
Zhu0lPouHYdB9QYRuUcMQP03UcZNyFsdmw1epVLfL3QP9TzDoeLBopu/gHNARUzp
Icx7rqme633XCldmnLn91CMGBOMGLQGdC+z16e9zQGYuliE/SfB66Kebz2f8ZBpK
Dqw5Riu8BQAPMK1kt9evb7L/a7TZD5ISlh253ES9Tmi8/Nxot7hGMuHXFvEdajyK
qwcTZ2vegt8Tu6Hb7199
=S6GG
-----END PGP SIGNATURE-----

```

</details>

[Email (text)](txt/email.txt)

## Solving

To solve this, you need to break the RSA private key. Doing this requires a fair bit of computing power. To crack `n`
we need to factorize it into its two smaller primes, `p` and `q`.

### The Math

The [number fieid sieve algorithm](https://en.wikipedia.org/wiki/General_number_field_sieve) was used to attack `n`.

The prime factors after attacking with the [NFS](https://en.wikipedia.org/wiki/General_number_field_sieve) algorithm:

```

p = 94424081139901371883469166542407095517576260048697655243
q = 79084622052242264844238683495727691663247340251867615781

```

Now to get the private key we need to solve for the secret exponent, `d`.

```

phi = (p-1)(q-1) = 7467492769579356967270197440403790283193525917787433197058250305765111796388761610844354228288301399878958918760
d = 65537-1 (mod phi) = 6095845029215954627034931303907142169470229688202235204684671759588136716587612454316830292189081535500929599993

```

### TODO How it was solved computationally with a better title

## What Happened

After solvers submitted their number to [http:// http://sq6wmgv2zcsrix6t.onion/NUM](../06.onion) they received an email for [MIDI puzzle](../08.midi); 

### TODO could only submit once? (not sure if this year)

### TODO what were the details of submitting? post request? submission form? page samples

## References

### Math

* [Number Fieid Sieve Algorithm](https://en.wikipedia.org/wiki/General_number_field_sieve)

### TODO

TODO Previous Next

