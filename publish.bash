now="$(date +'%d/%m/%Y %Hh %mm %Ss')"

#python fetchposts.py

rm -rf deploy

mkdir deploy

pelican -o deploy -s publishconf.py

git checkout -b gh-pages --track destiny/main

ghp-import deploy -b gh-pages -m "Publicado em $now" --cname=geracaoh2v.github.io

git push git@github.com:cochonilha/geracaoh2v.github.io.git gh-pages:main

