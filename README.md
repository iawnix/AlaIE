# AlaIE
- author: Iawnix
- date: 2025-11-29

1. 参考Z. H. Zhang等人JCTC的工作[DOI: 10.1021/acs.jctc.7b01295]
2. 计算原理:
- $$IE = KT \left[ \ln \left\langle e^{\beta \Delta E^{a}_{\text{int}}} \right\rangle - \ln \left\langle e^{\beta \Delta E^{x}_{\text{int}}} \right\rangle \right]$$
- $$\left\langle e^{\beta \Delta E^{x}_{\text{int}}} \right\rangle = \frac{1}{N} \sum_{i=1}^{N} e^{\beta \Delta E^{x}_{\text{int}}(t_{i})}$$
- $$\Delta E^{x}_{\text{int}}(t_{i}) = E^{x}_{\text{int}}(t_{i}) - \left\langle E^{x}_{\text{int}} \right\rangle$$
- $$E_{\text{int}} = E^{\text{vac}}_{\text{ele}} + E^{\text{vac}}_{\text{vdW}}$$
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

