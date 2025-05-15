# -*- mode: python -*-

Command(target=['#out/gen/hopscotchCommit.txt'],
        source=['.git/logs/HEAD'],
        action='git rev-parse HEAD > $TARGETS')

Command(target=['#out/gen/primordialsoupCommit.txt'],
        source=['.git/logs/HEAD'],
        action='git -C primordialsoup rev-parse HEAD > $TARGETS')

def BuildSnapshots(compiler_snapshot, sources, triples):
  host_vm = File('#out/ReleaseHost/primordialsoup')
  cmd = [host_vm.path, compiler_snapshot.path]
  cmd += [source.path for source in sources]

  snapshots = []
  for triple in triples:
    snapshot = File('#out/snapshots/' + triple[2])
    snapshots += [snapshot]
    cmd += [triple[0], triple[1], snapshot.path]

  Command(target=snapshots, source=sources, action=' '.join(cmd))
  Requires(snapshots, host_vm)
  Depends(snapshots, compiler_snapshot)

def BuildStage1Snapshots(triples):
  BuildSnapshots(File('primordialsoup/snapshots/compiler.vfuel'),
                 Glob('primordialsoup/newspeak/*.ns') + [File('src/WebCompiler.ns')],
                 triples)

def BuildStage2Snapshots(triples):
  sources = Glob('primordialsoup/newspeak/*.ns')
  sources += Glob('src/*.ns')
  sources += Glob('src/*.webp')
  sources += Glob('#out/gen/*.txt')
  sources += [File('CodeMirror/lib/codemirror.js')]
  sources += [File('CodeMirror/lib/codemirror_css.css')]
  BuildSnapshots(File('#out/snapshots/WebCompiler.vfuel'), sources, triples)

SConscript("primordialsoup/SConstruct")

BuildStage1Snapshots([
    ['RuntimeWithMirrors', 'WebCompiler', 'WebCompiler.vfuel'],
])

BuildStage2Snapshots([
    ['Runtime', 'Particles', 'Particles.vfuel'],
    ['RuntimeWithMirrors', 'HopscotchIDE', 'HopscotchIDE.vfuel.bmp'],
    ['RuntimeWithMirrors', 'HopscotchTestRunner', 'HopscotchTestRunner.vfuel'],
])

# All this moving outputs around is to make load-time relative paths agree with
# build-time relative paths. Eventually this should be handled by WebCompiler
# when we have I/O libraries.
Install("#out/site",
        ["#out/ReleaseEmscriptenWASM/primordialsoup.html",
         "#out/ReleaseEmscriptenWASM/primordialsoup.wasm",
         "#out/ReleaseEmscriptenWASM/primordialsoup.js",
         "#out/snapshots/HopscotchIDE.vfuel.bmp",
         "#out/snapshots/Particles.vfuel",
         "#out/snapshots/TestRunner.vfuel",
         "#out/snapshots/BenchmarkRunner.vfuel",
         "src/index.html",
         "CodeMirror"])
Install("#out/site/src", Glob("src/*.webp"))
