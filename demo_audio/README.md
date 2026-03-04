# Demo Audio Files

## Where to Get Sample Audio Files

### 1. Xeno-Canto (Bird Sounds)
The world's largest collection of bird sounds.

**Website:** https://xeno-canto.org/

**Recommended European Species to Test:**
- European Robin (Erithacus rubecula): https://xeno-canto.org/explore?query=erithacus+rubecula
- Common Blackbird (Turdus merula): https://xeno-canto.org/explore?query=turdus+merula
- Common Chaffinch (Fringilla coelebs): https://xeno-canto.org/explore?query=fringilla+coelebs
- Eurasian Wren (Troglodytes troglodytes): https://xeno-canto.org/explore?query=troglodytes+troglodytes

**How to Download:**
1. Click on any recording
2. Click the "Download" button
3. Save as WAV or MP3
4. Upload to EcoSound Monitor

### 2. BTO Acoustic Pipeline (UK Birds)
**Website:** https://www.bto.org/

### 3. Cornell Lab of Ornithology
**Website:** https://www.birds.cornell.edu/home/

### 4. Bat Call Library
For bat audio samples:
- **Bat Conservation Trust**: https://www.bats.org.uk/
- **Open Acoustic Devices**: https://www.openacousticdevices.info/

## Testing Tips

1. **Start with clear recordings** - Single species, minimal background noise
2. **Try different habitats** - Forest, wetland, urban
3. **Test various durations** - 10s to 60s clips work best
4. **Check file formats** - WAV preferred, MP3 also works

## Expected Results

When you upload a bird recording, you should see:
- Species name (scientific + common)
- Confidence score (higher is better)
- Detection timestamp
- Charts showing species distribution
- Downloadable PDF compliance report

## Note

The current MVP uses BirdNET for bird detection which works very well.
Bat detection is currently simulated for demo purposes - a production version 
would integrate BatDetect2 or similar validated models.
