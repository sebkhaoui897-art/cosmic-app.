      - name: Build APK with Buildozer
        run: |
          buildozer init || true
          sed -i 's/#title = My Application/title = Cosmic Guide/' buildozer.spec
          sed -i 's/#package.name = myapp/package.name = cosmicguide/' buildozer.spec
          sed -i 's/#package.domain = org.test/package.domain = org.cosmic/' buildozer.spec
          sed -i 's/#source.include_exts = py,png,jpg,kv,atlas/source.include_exts = py/' buildozer.spec
          sed -i 's/#source.main_filename = main.py/source.main_filename = main.py/' buildozer.spec
          sed -i 's/#requirements = python3,kivy/requirements = python3/' buildozer.spec
          buildozer -v android debug
