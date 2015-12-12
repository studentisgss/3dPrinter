
help:
	@echo "Use 'make slic3r' or 'make printrun'"

slic3r:
	@echo "(*) Starting Slic3r..."
	./slic3r/bin/slic3r --gui --load config/slic3r_pla.ini

printrun:
	@echo "(*) Starting Printrun..."
	@touch config/printrun.user~
	./printrun/pronterface.py --verbose \
		--config config/printrun.conf --config config/printrun.user~

.PHONY: slic3r printrun
