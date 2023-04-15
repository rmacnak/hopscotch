# -*- mode: python -*-

def BuildStage1Snapshots(host_vm, triples):
  cmd = [host_vm.path]

  compiler_snapshot = File('primordialsoup/snapshots/compiler.vfuel')
  cmd += [compiler_snapshot.path]

  sources = Glob('primordialsoup/newspeak/*.ns') + Glob('src/*.ns')
  cmd += [source.path for source in sources]

  snapshots = []
  for triple in triples:
    snapshot = File('#out/snapshots/' + triple[2])
    snapshots += [snapshot]
    cmd += [triple[0], triple[1], snapshot.path]

  Command(target=snapshots, source=sources, action=' '.join(cmd))
  Requires(snapshots, host_vm)
  Depends(snapshots, compiler_snapshot)


def BuildStage2Snapshots(host_vm, triples):
  cmd = [host_vm.path]

  compiler_snapshot = File('#out/snapshots/WebCompiler.vfuel')
  cmd += [compiler_snapshot.path]

  sources = Glob('primordialsoup/newspeak/*.ns')
  sources += Glob('src/*.ns')
  sources += Glob('src/*.webp')
  sources += [File('CodeMirror/lib/codemirror.js')]
  sources += [File('CodeMirror/lib/codemirror_css.css')]
  sources += [File('CodeMirror/addon/display/autorefresh.js')]
  cmd += [source.path for source in sources]

  snapshots = []
  for triple in triples:
    snapshot = File('#out/snapshots/' + triple[2])
    snapshots += [snapshot]
    cmd += [triple[0], triple[1], snapshot.path]

  Command(target=snapshots, source=sources, action=' '.join(cmd))
  Requires(snapshots, host_vm)
  Depends(snapshots, compiler_snapshot)


SConscript("primordialsoup/SConstruct")
host_vm = File('#out/ReleaseHost/primordialsoup')
BuildStage1Snapshots(host_vm, [
    ['RuntimeWithMirrors', 'WebCompiler', 'WebCompiler.vfuel'],
])
BuildStage2Snapshots(host_vm, [
    ['Runtime', 'Particles', 'Particles.vfuel'],
    ['RuntimeWithMirrors', 'HopscotchIDE', 'HopscotchIDE.vfuel'],
    ['RuntimeWithMirrors', 'HopscotchTestRunner', 'HopscotchTestRunner.vfuel'],
])
