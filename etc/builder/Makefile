all: clean build

ABR_DIR := ./abr_flow
ABR_LABEL := abr
ABR_TMPL := abr.yaml.in

RTA_DIR := ~/webhooks/flows/rta/$(bandwidth)/$(server)
RTA_LABEL := real-time-aud
RTA_TMPL := real-time-aud.yaml.in

GREED_DIR := ~/webhooks/flows/greedy/$(bytes)/$(server)
GREED_LABEL := greedy
GREED_TMPL := greedy.yaml.in

RTV_DIR := ~/webhooks/flows/rtv/$(bandwidth)/$(server)
RTV_LABEL := real-time-vid
RTV_TMPL := real-time-vid.yaml.in

SCAV_DIR := ~/webhooks/flows/scavenger/$(bandwidth)/$(server)
SCAV_LABEL := scavenger
SCAV_TMPL := scavenger.yaml.in

build: build-abr build-rta build-greed build-rtv build-scav

# ABR
build-abr:
	@./builder.py \
		--port $(port) \
		--label $(ABR_LABEL) \
		--template $(ABR_TMPL) \
		--server $(server) \
		--dest_dir $(ABR_DIR)

build-rta:
	@./builder.py \
                --port $(port) \
                --label $(RTA_LABEL) \
                --template $(RTA_TMPL) \
                --dest_dir $(RTA_DIR) \
		--server $(server) \
		--bandwidth $(bandwidth)

build-greed:
	@./builder.py \
		--port $(port) \
		--label $(GREED_LABEL) \
		--template $(GREED_TMPL) \
		--dest_dir $(GREED_DIR) \
		--server $(server) \
		--n_bytes $(bytes)

build-rtv:
	@./builder.py \
                --port $(port) \
                --label $(RTV_LABEL) \
                --template $(RTV_TMPL) \
                --dest_dir $(RTV_DIR) \
		--server $(server) \
		--bandwidth $(bandwidth)

build-scav:
	@./builder.py \
		--port $(port) \
		--label $(SCAV_LABEL) \
		--template $(SCAV_TMPL) \
		--dest_dir $(SCAV_DIR) \
		--server $(server) \
		--bandwidth $(bandwidth)


clean-abr: ; @$(RM) $(ABR_DIR)/*.yaml
clean-rta: ; @$(RM) $(RTA_DIR)/*.yaml
clean-greed: ; @$(RM) $(GREED_DIR)/*.yaml
clean-rtv: ; @$(RM) $(RTV_DIR)/*.yaml
clean-scav: ; @$(RM) $(SCAV_DIR)/*.yaml

.PHONY: clean clean-abr clean-rta clean-greed clean-rtv clean-scav build build-abr build-rta build-greed build-rtv build-scav
