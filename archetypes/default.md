---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
# 현재 생성되는 폴더의 부모 폴더 이름을 자동으로 가져와서 series에 넣습니다.
series: ["{{ index (split .Dir "/") (sub (len (split .Dir "/")) 2) }}"]
#series_order: 1
draft: false
---
