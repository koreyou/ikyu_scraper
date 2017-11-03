# I have not actually tried out Makefile, so it may have a bug

BUILDDIR = build

all : $(BUILDDIR)/json_dir

$(BUILDDIR) :
	mkdir -p $BUILDIR

$(BUILDDIR)/ikyu-area.txt : $(BUILDDIR)
	python get_last_link_list.py https://www.ikyu.com/ap/srch/UspW15001.aspx | tee $@

$(BUILDDIR)/url_list.txt : $(BUILDDIR)/ikyu-area.txt
	python download_hotel_urls.py $^ | tee $@

$(BUILDDIR)/html_dir : $(BUILDDIR)/url_list.txt
	python dl.py $^ $@

$(BUILDDIR)/json_dir : $(BUILDDIR)/html_dir
	bash scrape_all.sh $^ $@

clean :
	rm -rf $(BUILDDIR)
