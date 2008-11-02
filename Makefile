NAME=$(shell grep ^Name: *spec|cut -f2 -d\  )
VERSION=$(shell grep ^Version: *spec|cut -f2 -d\  )
DIR=$(NAME)-$(VERSION)
TAR=$(DIR).tar.gz
TAR_ORIG=$(NAME)_$(VERSION).orig.tar.gz
BUILDDIR=build
DESTDIR=$(BUILDDIR)

FILES=$(wildcard src/*)
MANFILES=$(wildcard man/*)
DOCFILES=COPYING README

BINDIR=/usr/sbin
DOCDIR=/usr/share/doc/$(DIR)
MANDIR=/usr/share/man/man8

all: $(FILES)
	echo "No compilation necessary."

install: $(FILES)
	mkdir -p $(DESTDIR)$(BINDIR)
	cp $(FILES) $(DESTDIR)$(BINDIR)
	mkdir -p $(DESTDIR)$(DOCDIR)
	cp $(DOCFILES) $(DESTDIR)$(DOCDIR)
	mkdir -p $(DESTDIR)$(MANDIR)
	cp $(MANFILES) $(DESTDIR)$(MANDIR)

clean:
	rm -rf $(BUILDDIR)
	rm -f $(TAR)
	rm -f ../$(DIR)

tar: clean
	ln -sf $(NAME) ../$(DIR)
	tar cCzf .. $(TAR) $(DIR) --exclude CVS --exclude .git --exclude $(TAR) --exclude $(BUILDDIR) --exclude debian --dereference
	rm -f ../$(DIR)

rpm: tar
	rpmbuild -ts $(TAR)

deb: tar
	mkdir -p $(BUILDDIR)
	tar xCzf $(BUILDDIR) $(TAR)
	mv $(TAR) $(BUILDDIR)/$(TAR_ORIG)
	cp -av debian/ $(BUILDDIR)/$(DIR)
	(cd $(BUILDDIR)/$(DIR) && dpkg-buildpackage -rfakeroot)
	rm -r $(BUILDDIR)/$(DIR)
