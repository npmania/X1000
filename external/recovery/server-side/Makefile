TOPDIR := $(shell pwd)/
OUTDIR := $(TOPDIR)/recovery-update
IMAGE_SRC ?= $(TOPDIR)/image
RES_SRC := $(TOPDIR)/../resource
SECURITY := $(RES_SRC)/security
KEYNAME := testkey
SOURCE := pack.sh

all: update.bin

update.bin: firmware_v0.tar.gz firmware_v0.info
	tar cf update.bin firmware_v0.tar.gz firmware_v0.info

firmware_v0.tar.gz: $(SOURCE)
	@./$(SOURCE) $(OUTDIR) $(IMAGE_SRC) $(SECURITY) $(KEYNAME)
	tar cf firmware_v0.tar.gz recovery-update

define INFO_TEXT
M0 Pro
V1.5
$(shell md5sum firmware_v0.tar.gz)
endef
export INFO_TEXT

firmware_v0.info: firmware_v0.tar.gz
	echo "$$INFO_TEXT" > firmware_v0.info

clean:
	@rm -rf $(OUTDIR) update.bin firmware_v0.tar.gz firmware_v0.info

.PHONY: all clean
