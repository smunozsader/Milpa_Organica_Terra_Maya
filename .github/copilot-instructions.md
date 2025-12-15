# Terra Maya Orgánica - AI Coding Agent Instructions

## Project Context
This is an agricultural productivity and infrastructure planning project for **Terra Maya Orgánica**, an organic poultry farm in Yucatán, Mexico. The project models a technified organic milpa system (intercropped corn/beans/squash) and analyzes the equipment acquisition strategy for establishing a 20-hectare pilot phase, scalable to 250 ha.

**Business Goals**: 
1. Calculate crop yields to support self-sufficiency in poultry feed (corn fodder via FVH) and commercial sales (Jamapa beans, squash seeds)
2. Optimize equipment investment strategy (own vs rent) for excavation and land clearing
3. Minimize time to first harvest while maximizing ROI

**Project Scope:**
- **Phase 1 (current):** 20 hectares pilot implementation
- **Future expansion:** 100-250 hectares total capacity
- **Timeline:** 4 years to complete 20 ha with staggered subsections
- **First harvest:** Month 17 from project start

## Core Architecture

### Multi-Component Project Structure

This project consists of:

1. **Python Productivity Calculator** - [`milpa_productividad.py`](milpa_productividad.py)
   - Standalone script for crop yield calculations
   - Embedded documentation for agronomist use
   - Direct console output, no databases

2. **LaTeX Technical Documentation** (3 main documents):
   - **[`analisis_tiempos_excavacion.tex`](analisis_tiempos_excavacion.tex)** (1,773 lines, 34 pages PDF)
     * MASTER REFERENCE document for equipment strategy
     * Analyzes 5 scenarios: rent all, buy 1 retro, buy 2 retros, buy 4 retros, mixed strategy
     * **Recommendation:** Buy 2 CAT 420F retroexcavadoras + FAE forestry mulcher attachment
     * Includes complete land clearing (desmonte) analysis: 3 options compared
     * Detailed ROI calculations, breakeven analysis, timeline chronograms
   
   - **[`reporte_proyeccion_5anos.tex`](reporte_proyeccion_5anos.tex)** (766 lines, 18 pages PDF)
     * 5-year financial projection for investors/stakeholders
     * Revenue streams by crop, cost structure, cash flow analysis
     * Includes updated equipment investment and organic land clearing section
   
   - **[`validacion_tecnica_academica.tex`](validacion_tecnica_academica.tex)** (1,089 lines, 22 pages PDF)
     * Academic/technical validation of SPCM system assumptions
     * Validates excavation costs against CICY research data
     * Equipment investment justification with technical specifications
     * Organic certification requirements (no-burn land clearing)

3. **Supporting Documentation:**
   - [`terra_maya_conversacion.txt`](terra_maya_conversacion.txt): Project rationale, SPCM research summary
   - [`MEMORIA_CALCULO_PUNTO_EQUILIBRIO.md`](MEMORIA_CALCULO_PUNTO_EQUILIBRIO.md): Detailed breakeven calculation audit
   - [`CONSISTENCIA_DOCUMENTOS.md`](CONSISTENCIA_DOCUMENTOS.md): Cross-document consistency verification report
   - [`costo_pocetas.txt`](costo_pocetas.txt): Initial excavation cost estimates
   - `2025. maiz continuo/*.pdf`: SPCM scientific papers (CICY researchers)

### Equipment Acquisition Strategy (FINAL DECISION)

**Approved Strategy:** Buy 2 CAT 420F retroexcavadoras + FAE DML/HY forestry mulcher attachment

**Investment Breakdown:**
- 2 CAT 420F used backhoes (2015-2018 models): **$3,160,000 MXN**
  * Excavator 1: $1,450,000 + $85,000 transport + $45,000 inspection = $1,580,000
  * Excavator 2: Same breakdown = $1,580,000
- FAE DML/HY hydraulic forestry mulcher: **$235,000 MXN**
- **Total equipment investment: $3,395,000 MXN**

**Key advantages of this strategy:**
- Two excavators work together on each 5-ha subsection → complete in 12 months
- Staggered implementation: 4 subsections × 5 ha → first harvest month 17
- FAE attachment mounts on either excavator (5-minute hydraulic coupling)
- No-burn organic land clearing (certification requirement)
- One operator per machine (FAE uses excavator operator, no extra personnel)
- ROI incremental (2nd excavator): **3,425%**
- Savings vs renting all equipment: **$310,000** for 20 ha
- FAE savings vs Vermeer BC1000XL independent chipper: **$187,080**

### Organic Land Clearing (Desmonte Orgánico)

**Requirement:** Organic certification **prohibits burning** vegetation. Fields have secondary growth (acahual) that must be cleared before excavation.

**Solution adopted: FAE DML/HY Forestry Mulcher Attachment**

**3 Options Analyzed:**
| Option | Investment | Total Cost (20 ha) | Advantage |
|--------|-----------|-------------------|-----------|
| A: Rent chipper | $0 | $314,912 | No capital commitment |
| B: Buy Vermeer BC1000XL | $405,000 | $521,912 | Independent equipment |
| **C: FAE attachment** ✓ | **$235,000** | **$333,912** | **Integrated, flexible** |

**FAE DML/HY Specifications:**
- Type: Hydraulic forestry mulcher for CAT 420F backhoe
- Rotor: 1,200 RPM with tungsten carbide teeth
- Capacity: Vegetation up to 20 cm diameter
- Mounting: Quick-coupler, 5-minute setup on either excavator
- Performance: 0.8 ha/day (10 days per 5-ha subsection = 0.3 months)
- Maintenance: $1,200 per subsection (vs $2,500 for Vermeer)

**7 Key Advantages over Vermeer:**
1. Integration: Mounts on existing excavators (not standalone equipment)
2. Personnel: Uses same excavator operator (saves $12,800/subsection vs Vermeer's 2-person crew)
3. Lower investment: $235k vs $405k (42% cheaper)
4. Operational flexibility: While one excavator mulches, other can start excavating
5. Transport included: No dedicated trailer needed
6. Scalability: Breakeven 47.6 ha; saves $2.1M in 250 ha expansion
7. Agronomic benefit: Mulch improves 23% moisture retention in limestone soils

### Domain-Specific Calculations (SPCM System)
Based on SPCM (Sistema de Producción Continua de Maíz) research validated in Yucatán's limestone soils:
- **Pocetas system**: 22,000 planting holes/ha with substrate mix (chicken manure + coconut husk)
- **Polycropping**: 3 corn + 2 bean + 0.5 squash seeds per hole (intercropping pattern)
- **3 cycles/year**: Enabled by drip irrigation + fertigation in tropical climate (no frost)

### Implementation Timeline (4-Year Staggered Model)

**Process per 5-ha subsection:**
1. **Desmonte (FAE mulcher):** 0.3 months (10 days)
2. **Excavación (2 retros together):** 12 months (110,000 pocetas)
3. **Siembra (planting):** Immediate after excavation complete
4. **Primera cosecha (first harvest):** +4 months from planting

**Staggered schedule (20 ha = 4 subsections):**
- Subsection 1: Clearing month 0.0 → Excavation 0.3-12.3 → **Harvest month 17**
- Subsection 2: Clearing month 12.3 → Excavation 12.6-24.6 → **Harvest month 29**
- Subsection 3: Clearing month 24.6 → Excavation 24.9-36.9 → **Harvest month 41**
- Subsection 4: Clearing month 36.9 → Excavation 37.2-49.2 → **Harvest month 54**

**Critical milestone:** First revenue at month 17 (vs month 46 with 1 excavator strategy)

### Cost Structure (20 ha Phase 1)

**Initial Investment:**
- Equipment: $3,395,000 (2 retroexcavadoras + FAE attachment)
- FVH module: $250,000 (pilot hydroponic fodder system)
- **Total equipment: $3,645,000**

**Per-Hectare Infrastructure Costs:**
- Organic land clearing (FAE): $24,700/ha
- Excavation (2 retros, 22k pocetas): $251,800/ha
- Organic substrate: $44,000/ha
- Drip irrigation system: $45,000/ha
- Deep well + pump: $100,000/ha (shared infrastructure)
- **Total infrastructure: ~$465,500/ha**

**For 20 ha:**
- Desmonte: $494,000 (20 ha × $24,700)
- Excavación: $5,036,000 (20 ha × $251,800)
- Sustrato: $880,000
- Riego: $900,000
- Pozos: $2,000,000
- Equipment: $3,645,000
- **Total investment: ~$13M MXN** (equipment + infrastructure)

**Operational Costs (annual/ha):**
- Seeds: $3,000
- Organic fertilizers: $8,000
- Irrigation operation: $5,000
- Labor (3 cycles): $25,000
- **Total: $41,000/ha/year**

## Python Calculator (`milpa_productividad.py`)

### Single-File Calculator Pattern
- Main logic in [`milpa_productividad.py`](milpa_productividad.py) - a standalone Python script with embedded documentation
- **NOT** a multi-module system - all calculations in one file for easy sharing with agronomists
- Output format: Direct console prints, no persistent storage or APIs
- **Note:** Old file `ilpa_productividad.py` was deleted as duplicate

## Key Conventions

### Variable Naming (Spanish Agricultural Terms)
- `pocetas_por_ha` = planting holes per hectare (not "pockets")
- `rend_*` prefix = rendimiento (yield), e.g., `rend_maiz_anual`
- `plantas_*_ha` = established plants per hectare after survival rate
- Use Spanish for domain terms; English for code structure (`for`, `if`, etc.)

### Editable Parameters Section
**Always maintain** the top block (lines 4-17) as user-modifiable:
```python
# Parámetros editables
pocetas_por_ha = 22000
semillas_maiz_por_poceta = 3
...
```
Agronomists adjust these values directly - treat as configuration interface.

### Yield Calculations
- Per-plant yields (`rend_*_por_planta_ciclo`) are calibrated to SPCM research targets:
  - Corn: 3.5 t/ha/cycle → ~0.000066 t/plant (52,800 plants/ha)
  - Bean: 1.3 t/ha/cycle → ~0.000037 t/plant
  - Squash: Based on fruit-to-seed conversion (10% seed weight)
- **Critical**: Annual yield = `plants/ha × yield/plant × 3 cycles`

## Development Workflows

### Running Calculations
```powershell
# No virtual environment needed - uses system Python
python milpa_productividad.py
```
Expected output format:
```
=== PRODUCTIVIDAD MILPA TECNIFICADA ===
Plantas/ha: Maíz 52800, Frijol 35200, Calabaza 8800
Rendimiento anual (t/ha): Maíz 10.5, Frijol 3.9, Calabaza 12.0
...
```

### Compiling LaTeX Documents
```powershell
# Always compile TWICE for cross-references
pdflatex -interaction=nonstopmode analisis_tiempos_excavacion.tex
pdflatex -interaction=nonstopmode analisis_tiempos_excavacion.tex

pdflatex -interaction=nonstopmode reporte_proyeccion_5anos.tex
pdflatex -interaction=nonstopmode reporte_proyeccion_5anos.tex

pdflatex -interaction=nonstopmode validacion_tecnica_academica.tex
pdflatex -interaction=nonstopmode validacion_tecnica_academica.tex
```

### Testing Changes
- Modify parameters → run script → verify output matches agronomic logic
- Cross-reference results with `terra_maya_conversacion.txt` (baseline assumptions)
- No automated tests - validation via domain expert review

## Reference Materials

### Supporting Documents (Read-Only Context)
- [`terra_maya_conversacion.txt`](terra_maya_conversacion.txt): Project rationale, SPCM research summary, and yield targets
- `2025. maiz continuo/*.pdf`: SPCM scientific papers from CICY researchers (Larqué Saavedra et al.)
- `2025. folletos web site pollos/`: Terra Maya Orgánica marketing materials

### Critical Assumptions to Preserve
1. **80% survival rate** - conservative for direct organic seeding
2. **3 cycles/year** - validated by Yucatán's year-round growing season
3. **Limestone soil (litosol)** - requires substrate-filled pocetas, not standard tillage

## Common Modifications

### Adjusting Crop Mix
To change seeding rates (e.g., more beans, less squash):
1. Edit `semillas_*_por_poceta` values
2. Verify `plantas_*_ha` calculations update correctly
3. Check `supervivencia` still applies uniformly (or split by crop if needed)

### Scaling to Full 250 ha
Replace `ha_lote = 20` with target area. Note: Script currently shows Phase 1 (20 ha); full deployment data in conversation file.

### Adding New Crops
Follow pattern:
```python
semillas_CULTIVO_por_poceta = X
plantas_CULTIVO_ha = pocetas_por_ha * semillas_CULTIVO_por_poceta * supervivencia
rend_CULTIVO_por_planta_ciclo = Y  # Calibrate to research
rend_CULTIVO_anual = plantas_CULTIVO_ha * rend_CULTIVO_por_planta_ciclo * ciclos_por_ano
```

## Expected Future Enhancements

### Cost Analysis Integration
- **Source data**: See [`MEMORIA_CALCULO_PUNTO_EQUILIBRIO.md`](MEMORIA_CALCULO_PUNTO_EQUILIBRIO.md) for detailed breakeven analysis
- **Current strategy costs (Phase 1 - 20 ha):**
  * Equipment: $3,395,000 (2 retros + FAE)
  * Desmonte: $24,700/ha ($494,000 total)
  * Excavation: $251,800/ha ($5,036,000 total)
  * Substrate: $44,000/ha
  * Drip irrigation: $45,000/ha
- **Implementation pattern**: Equipment costs are sunk; focus on per-hectare operational costs for expansion scenarios
- Example addition to Python calculator:
```python
# Costos (MXN/ha) - ACTUALIZADO CON ESTRATEGIA 2 RETROS + FAE
costo_desmonte_ha = 24700  # FAE forestry mulcher
costo_excavacion_ha = 251800  # 2 retroexcavadoras trabajando juntas
costo_sustrato_ha = 44000
costo_riego_ha = 45000
costo_total_infraestructura_ha = costo_desmonte_ha + costo_excavacion_ha + costo_sustrato_ha + costo_riego_ha
# Calculate total investment and per-ton production cost
```

### Multi-Year Projections
- Model yield improvements from soil buildup (year 2+ with biofábricas)
- Account for substrate degradation/replenishment cycles
- Project revenue streams: poultry feed (internal), Jamapa beans, squash seeds (external sales)
- Consider SADER subsidy scenarios for capital costs

### Export Formats for Business Planning
- **CSV export**: Annual yields by crop and total revenue for spreadsheet analysis
- **Excel integration**: Formatted tables with cost/benefit ratios for stakeholder reports
- **Example implementation**:
```python
import csv
with open('reporte_anual.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Cultivo', 'Plantas/ha', 'Rend t/ha/año', 'Total 20 ha'])
```

## Calculation Validation Rules

### Realistic Yield Constraints
- **Corn max**: 10.5 t/ha/year (3.5 t/cycle × 3) - validated by SPCM in optimal conditions
- **Bean max**: 4.5 t/ha/year (1.5 t/cycle × 3) - upper bound for intercropped organic systems
- **Squash warning**: If `rend_calabaza_anual > 15 t/ha`, flag as unrealistic for Yucatán climate
- **Survival rate range**: 0.6-0.9 (below 60% indicates seeding/soil problems; above 90% unlikely in direct seeding)

### Input Validation Patterns
Add these checks before calculations:
```python
# Validate pocetas density
if pocetas_por_ha < 15000 or pocetas_por_ha > 30000:
    print(f"⚠️ ADVERTENCIA: Densidad {pocetas_por_ha} pocetas/ha fuera de rango típico (15k-30k)")

# Validate survival
if supervivencia < 0.6 or supervivencia > 0.9:
    print(f"⚠️ ADVERTENCIA: Supervivencia {supervivencia*100}% inusual para siembra directa")
```

### Cross-Crop Consistency
- Total seeds per poceta should match physical space: `(maíz + frijol + calabaza) × seed_size < poceta_volume`
- Corn:bean ratio typically 3:2 or 2:1 in traditional milpa - flag if bean > corn plants

### Edge Cases to Handle
1. **Zero cycles**: If `ciclos_por_ano < 1`, system reverts to traditional milpa (document this mode)
2. **Partial hectares**: Script currently uses `ha_lote = 20`; ensure calculations work for fractional ha (test plots)
3. **Missing irrigation**: Without fertigation, reduce `ciclos_por_ano` to 1 and yields to traditional levels

## Output Formatting Guidance

### Console Output Standards
Current format is stakeholder-friendly. When enhancing:
- Keep Spanish headers: `=== PRODUCTIVIDAD MILPA TECNIFICADA ===`
- Use thousand separators for large numbers: `{value:,.0f}` instead of `{value:.0f}`
- Add units explicitly: `(t/ha)`, `(plantas/ha)`, `(MXN)`

### Progressive Enhancement Pattern
```python
# Basic: Current implementation
print(f"Rendimiento anual (t/ha): Maíz {rend_maiz_anual:.1f}")

# Enhanced: Add totals and comparisons
print(f"Rendimiento anual (t/ha): Maíz {rend_maiz_anual:.1f} (+{mejora_vs_tradicional:.0f}% vs milpa tradicional)")

# Advanced: Tabular format for multiple scenarios
print(f"{'Cultivo':<15} {'t/ha/año':>10} {'Total 20 ha':>12} {'Valor MXN':>12}")
```

### Business Report Templates
For stakeholder presentations, generate:
1. **Summary table**: Crop yields, revenue by product, ROI timeline
2. **Comparison view**: Technified milpa vs traditional (10x improvement)
3. **Sensitivity analysis**: Yield variations at ±20% survival rates

## AI Agent Best Practices
- **Preserve Spanish domain terms** - essential for end-user communication with agronomists
- **Show intermediate calculations** when modifying yields - helps validate agronomic logic
- **Reference SPCM data** from conversation file when explaining yield assumptions
- **Avoid over-engineering** - stakeholders prefer simple scripts over complex frameworks
- **Validate against real-world constraints** - flag unrealistic parameters before running calculations
- **Document assumptions clearly** - especially when extending beyond SPCM research scope

## Common Modifications

### Adjusting Equipment Strategy
If analyzing alternative equipment scenarios (1 retro, 4 retros, rent all):
1. Refer to [`analisis_tiempos_excavacion.tex`](analisis_tiempos_excavacion.tex) for complete analysis of 5 strategies
2. Update timeline calculations: 1 retro = 24 months/5ha, 2 retros = 12 months/5ha, 4 retros = 6 months/5ha
3. Recalculate first harvest timing: depends on when first subsection completes excavation
4. **Current approved strategy:** 2 retros + FAE attachment (optimal cost/time balance)

### Scaling Land Clearing Analysis
To evaluate desmonte for different hectare targets:
- **Base cost/ha:** $24,700 (FAE attachment)
- **Alternative costs:** Rent $15,746/ha, Vermeer ownership $26,096/ha
- **Breakeven FAE vs Vermeer:** 47.6 ha
- **For 250 ha expansion:** FAE saves $2.1M vs Vermeer, $333k vs renting

### Multi-Year Financial Projections
When extending [`reporte_proyeccion_5anos.tex`](reporte_proyeccion_5anos.tex):
- Year 1-4: Staggered implementation (subsections completing sequentially)
- First revenue: Month 17 (subsection 1 harvest)
- Cumulative revenue growth: Each subsection adds ~$1.8M/year at full production
- Equipment already paid: Use salvage value (70-80% after 3 years) for expansions
- Substrate replenishment: Budget $44k/ha every 3-4 years

## LaTeX Document Compilation

### PDF Generation Best Practices
When compiling LaTeX documents (`.tex` files) to PDF, **always compile TWICE** to ensure:
1. **First compilation:** Generates auxiliary files (.aux, .toc, .lof, .lot) with reference information
2. **Second compilation:** Resolves cross-references, table of contents, and index entries

**Example workflow:**
```powershell
# First compilation
pdflatex -interaction=nonstopmode document.tex

# Second compilation (resolves references)
pdflatex -interaction=nonstopmode document.tex
```

**Why this matters:**
- Single compilation leaves references as "??" or shows incorrect page numbers
- Table of contents (TOC) requires two passes to populate correctly
- Cross-references (\ref, \cite) need two passes to resolve
- Professional documents require fully resolved references for stakeholder review

**Special cases:**
- After adding new sections/figures/tables: Always recompile twice
- After bibliography changes: Compile → BibTeX → Compile → Compile (3 total)
- If using packages like `hyperref`: Second pass ensures proper link generation
