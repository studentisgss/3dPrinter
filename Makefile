
help:
	@echo "Use 'make slic3r' or 'make printrun'"

slic3r:
	@echo "(*) Starting Slic3r..."
	./slic3r/bin/slic3r --gui --load config/slic3r_pla.ini

printrun:
	@echo "(*) Starting Printrun..."
	./printrun/pronterface.py --verbose --config config/printrun.conf

.PHONY: slic3r printrun
