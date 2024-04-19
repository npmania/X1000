# default setting for partition.py, using to generate partition.conf
# exclusively ####
search_prefix = 're_'
# nor flash configuation
re_nand_tag = 'nand'
re_nand_device_size = '128MB'
re_nand_partition = (
                    ("uboot", "0x0", "0x100000", "mtdblock0"),
                    ("bt_mac", "0x100000", "0x20000", "mtdblock1"),
                    ("user_id", "0x120000", "0x20000", "mtdblock2"),
                    ("kernel", "0x140000", "0x600000", "mtdblock3"),
                    ("recovery", "0x740000", "0x800000", "mtdblock4"),
                    ("rootfs", "0xf40000", "0x5000000", "mtdblock5"),
                    ("data", "0x5f40000", "0x20c0000", "mtdblock6"),
)

local = locals()
