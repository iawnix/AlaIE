# AlaIE
- author: Iawnix
- date: 2025-11-29

1. 参考Z. H. Zhang等人JCTC的工作[DOI: 10.1021/acs.jctc.7b01295]
2. 计算原理:
- $IE = KT \left[ \ln \langle e^{\beta \Delta E^a_{\text{int}}} \rangle - \ln \langle e^{\beta \Delta E^x_{\text{int}}} \rangle \right]$
- $\langle e^{\beta \Delta E^x_{\text{int}}} \rangle = \frac{1}{N} \sum_{i=1}^N e^{\beta \Delta E^x_{\text{int}}(t_i)}$
- $\Delta E^x_{\text{int}}(t_i) = E^x_{\text{int}}(t_i) - \langle E^x_{\text{int}} \rangle$
- $E_{\text{int}}(t_i) = E^{\text{vac}}_{\text{ele}}(t_i) + E^{\text{vac}}_{\text{vdW}}(t_i)$
  
# Install
- `conda create -n AlaIE python=3.10`
- `conda activate AlaIE`
- `pip install .`

# Usage
- `AlaIE -h`

# Test
## Linux
- `cd ./test`
- `./run.sh`
## windows
- `mkdir out`
- `AlaIE -AlaDecPath ./data/ -T 300 -out test.txt -debug True`

