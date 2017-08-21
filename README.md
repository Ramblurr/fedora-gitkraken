# Update package

* Update package version in spec
* Download fresh source tarball

```$ spectool -fg *spec```

* Generate new checksums with

```$ sha512sum --tag gitkraken-amd64.tar.gz > sources```

* Build package

```$ fedpkg --dist f26 local```

* Install package

```$ dnf install ./x86_64/gitkraken-*.x86_64.rpm```
