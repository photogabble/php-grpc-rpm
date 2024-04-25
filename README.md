# PHP gRPC RPM Package

This repository is the result of my learning how to create a Linux RPM package. I needed to be able to easily install the PHP extension for [gRPC](https://grpc.io/) into a Elastic Beanstalk managed server running Amazon Linux 2.

I learned a lot from [Remi's RPM repository](https://blog.remirepo.net/) epecially their [source code for php-pecl-grpc](https://git.remirepo.net/cgit/rpms/php/pecl/php-pecl-grpc.git/).

This repository build an rpm package for [ext-grpc version 1.62.0](https://pecl.php.net/package/gRPC/1.62.0) for PHP 8.2. I'll keep it up to date with gRPC versions for as long as I make use of it.
